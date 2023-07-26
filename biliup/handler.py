import logging
import subprocess
from pathlib import Path

from . import plugins
from .downloader import download, check_url
from .engine import invert_dict, Plugin
from biliup.config import config
from .engine.event import Event, EventManager
from .uploader import upload
from functools import reduce

CHECK = 'check'
CHECK_UPLOAD = 'check_upload'
TO_MODIFY = 'to_modify'
DOWNLOAD = 'download'
BE_MODIFIED = 'be_modified'
UPLOAD = 'upload'
logger = logging.getLogger('biliup')


def create_event_manager():
    streamer_url = {k: v['url'] for k, v in config['streamers'].items()}
    inverted_index = invert_dict(streamer_url)
    urls = list(inverted_index.keys())
    pool1_size = config.get('pool1_size', 3)
    pool2_size = config.get('pool2_size', 3)
    # 初始化事件管理器
    app = EventManager(config, pool1_size=pool1_size, pool2_size=pool2_size)
    app.context['urls'] = urls
    app.context['url_status'] = dict.fromkeys(inverted_index, 0)
    app.context['checker'] = Plugin(plugins).sorted_checker(urls)
    app.context['inverted_index'] = inverted_index
    app.context['streamer_url'] = streamer_url
    return app


event_manager = create_event_manager()


@event_manager.register(DOWNLOAD, block='Asynchronous1')
def process(name, url):
    stream_info = {
        'name': name,
        'url': url,
    }
    try:
        kwargs: dict = config['streamers'][name].copy()
        kwargs.pop('url')
        suffix = kwargs.get('format')
        if suffix:
            kwargs['suffix'] = suffix
        stream_info = download(name, url, **kwargs)
    finally:
        return Event(UPLOAD, (stream_info,))


@event_manager.register(UPLOAD, block='Asynchronous2')
def process_upload(stream_info):
    url = stream_info['url']
    yield Event(BE_MODIFIED, (url, 2))
    try:
        upload(stream_info)
    finally:
        yield Event(BE_MODIFIED, args=(url, 0))


@event_manager.server()
class KernelFunc:
    def __init__(self, urls, url_status: dict, checker, inverted_index, streamer_url):
        self.urls = urls
        self.url_status = url_status
        self.__raw_streamer_status = url_status.copy()
        self.checker = checker
        self.inverted_index = inverted_index
        self.streamer_url = streamer_url

    @event_manager.register(CHECK, block='Asynchronous1')
    def singleton_check(self, platform):
        plugin = self.checker[platform]
        wait = config.get('checker_sleep', 15)
        for url in check_url(plugin, self.url_status, secs=wait):
            yield Event(TO_MODIFY, args=(url,))

    @event_manager.register(TO_MODIFY)
    def modify(self, url):
        if not url:
            return logger.debug('无人直播')
        if self.url_status[url] == 1:
            return logger.debug('已开播正在下载')
        if self.url_status[url] == 2 and not config.get('uploading_record'):
            return logger.debug('正在上传稍后下载')
        name = self.inverted_index[url]

        if config['streamers'].get(name, {}).get('preprocessor'):
            preprocessor(config['streamers'].get(name, {}).get('preprocessor'), f'{{"name": "{name}", "url": "{url}"}}')
        logger.debug(f'{name}刚刚开播，去下载')
        self.url_status[url] = 1
        return Event(DOWNLOAD, args=(name, url))

    @event_manager.register(CHECK_UPLOAD)
    def free_upload(self):
        for title, urls in self.streamer_url.items():
            if self.free(urls):
                yield Event(UPLOAD, args=({
                                              'name': title,
                                              'url': urls[0],
                                          },))

    @event_manager.register(BE_MODIFIED)
    def revise(self, url, status):
        if url:
            # 更新字典
            # url_status = {**url_status, **{url: 0}}
            self.url_status.update({url: status})

    def free(self, list_url):
        status_num = list(map(lambda x: self.url_status.get(x), list_url))
        return not (1 in status_num or 2 in status_num)

    def get_url_status(self):
        return self.url_status


def preprocessor(processors, data):
    for processor in processors:
        if processor.get('run'):
            try:
                process_output = subprocess.check_output(
                    processor['run'], shell = True,
                    input = data,
                    stderr = subprocess.STDOUT, text = True)
                logger.info(process_output.rstrip())
            except subprocess.CalledProcessError as e:
                logger.exception(e.output)
                continue

import inspect
import logging
import time

from biliup.config import config
from .engine.decorators import Plugin

logger = logging.getLogger('biliup')

def upload(data):
    """
    上传入口
    :param platform:
    :param index:
    :param data: 现在需包含内容{url,date} 完整包含内容{url,date,format_title}
    :return:
    """
    try:
        index = data['name']
        context = {**config, **config['streamers'][index]}
        platform = context.get("uploader", "biliup-rs")
        cls = Plugin.upload_plugins.get(platform)
        if cls is None:
            return logger.error(f"No such uploader: {platform}")
        streamer = data.get('streamer', index)
        date = data.get("date", time.localtime())
        title = data.get('title', index)
        url = data.get('url')
        live_cover_path = data.get('live_cover_path')
        data["format_title"] = custom_fmtstr(context.get('title', f'%Y.%m.%d{index}'), date, title, streamer, url)
        if context.get('description'):
            context['description'] = custom_fmtstr(context.get('description'), date, title, streamer, url)
        threshold = config.get('filtering_threshold', 0)
        if threshold:
            data['threshold'] = threshold
        data['dolby'] = config.get('dolby', 0)
        data['hires'] = config.get('hires', 0)
        data['no_reprint'] = config.get('no_reprint', 0)
        data['open_elec'] = config.get('open_elec', 0)
        sig = inspect.signature(cls)
        kwargs = {}
        for k in sig.parameters:
            v = context.get(k)
            if v:
                kwargs[k] = v
        return cls(index, data, **kwargs).start()
    except:
        logger.exception("Uncaught exception:")


def custom_fmtstr(string, date, title, streamer, url):
    return time.strftime(string.encode('unicode-escape').decode(), date).encode().decode("unicode-escape").format(title=title, streamer=streamer, url=url)

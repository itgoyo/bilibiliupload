import random
import subprocess
import time

import requests
import yt_dlp

from . import logger
from ..engine.decorators import Plugin
from ..engine.download import DownloadBase
from ..plugins import BatchCheckBase
from biliup.config import config
from biliup.plugins.Danmaku import DanmakuClient

VALID_URL_BASE = r'(?:https?://)?(?:(?:www|go|m)\.)?twitch\.tv/(?P<id>[0-9_a-zA-Z]+)'
_OPERATION_HASHES = {
    'CollectionSideBar': '27111f1b382effad0b6def325caef1909c733fe6a4fbabf54f8d491ef2cf2f14',
    'FilterableVideoTower_Videos': 'a937f1d22e269e39a03b509f65a7490f9fc247d7f83d6ac1421523e3b68042cb',
    'ClipsCards__User': 'b73ad2bfaecfd30a9e6c28fada15bd97032c83ec77a0440766a56fe0bd632777',
    'ChannelCollectionsContent': '07e3691a1bad77a36aba590c351180439a40baefc1c275356f40fc7082419a84',
    'StreamMetadata': '1c719a40e481453e5c48d9bb585d971b8b372f8ebb105b17076722264dfa5b3e',
    'ComscoreStreamingQuery': 'e1edae8122517d013405f237ffcc124515dc6ded82480a88daef69c83b53ac01',
    'VideoPreviewOverlay': '3006e77e51b128d838fa4e835723ca4dc9a05c5efd4466c1085215c6e437e65c',
}
_CLIENT_ID = 'kimne78kx3ncx6brgo4mv6wki5h1ko'


@Plugin.download(regexp=r'https?://(?:(?:www|go|m)\.)?twitch\.tv/(?P<id>[^/]+)/(?:videos|profile|clips)')
class TwitchVideos(DownloadBase):
    def __init__(self, fname, url, suffix='mp4'):
        DownloadBase.__init__(self, fname, url, suffix=suffix)

    def check_stream(self):
        with yt_dlp.YoutubeDL({'download_archive': 'archive.txt'}) as ydl:
            info = ydl.extract_info(self.url, download=False)
            for entry in info['entries']:
                if ydl.in_download_archive(entry):
                    continue
                self.raw_stream_url = entry['url']
                self.room_title = entry.get('title')
                ydl.record_download_archive(entry)
                return True

    class BatchCheck(BatchCheckBase):
        def __init__(self, urls):
            BatchCheckBase.__init__(self, pattern_id=VALID_URL_BASE, urls=urls)

        def check(self):
            with yt_dlp.YoutubeDL({'download_archive': 'archive.txt'}) as ydl:
                for channel_name, url in self.not_live():
                    info = ydl.extract_info(url, download=False, process=False)
                    for entry in info['entries']:
                        if ydl.in_download_archive(entry):
                            continue
                        yield url
                    time.sleep(10)
                    # ydl.record_download_archive(entry)

        def not_live(self):
            gql = self.get_streamer()
            i = -1
            for data in gql:
                i += 1
                user = data['data'].get('user')
                if not user:
                    continue
                stream = user['stream']
                if not stream:
                    yield self.usr_list[i], self.usr_dict.get(self.usr_list[i])

        def get_streamer(self):
            for channel_name in self.usr_list:
                op = {
                    'operationName': 'StreamMetadata',
                    'variables': {'channelLogin': channel_name.lower()}
                }
                op['extensions'] = {
                    'persistedQuery': {
                        'version': 1,
                        'sha256Hash': _OPERATION_HASHES[op['operationName']],
                    }
                }
                yield get_streamer(op)


@Plugin.download(regexp=VALID_URL_BASE)
class Twitch(DownloadBase):
    def __init__(self, fname, url, suffix='flv'):
        DownloadBase.__init__(self, fname, url, suffix=suffix)
        self.twitch_danmaku = config.get('twitch_danmaku', False)
        self.twitch_disable_ads = config.get('twitch_disable_ads', True)
        self.proc = None

    def check_stream(self):
        if not list(Twitch.BatchCheck([self.url]).check()):
            return
        gql = Twitch.BatchCheck([self.url]).get_streamer()
        for data in gql:
            self.room_title = data.get('data').get('user').get('lastBroadcast').get('title')
        if self.downloader == 'ffmpeg':
            port = random.randint(1025, 65535)
            stream_shell = [
                "streamlink",
                "--player-external-http",  # 为外部程序提供流媒体数据
                # "--twitch-disable-ads",                     # 去广告，去掉、跳过嵌入的广告流
                # "--twitch-disable-hosting",               # 该参数从5.0起已被禁用
                "--twitch-disable-reruns",  # 如果该频道正在重放回放，不打开流
                "--player-external-http-port", str(port),  # 对外部输出流的端口
                self.url, "best"  # 流链接
            ]
            if self.twitch_disable_ads:  # 去广告，去掉、跳过嵌入的广告流
                stream_shell.insert(1, "--twitch-disable-ads")
            twitch_cookie = config.get('user', {}).get('twitch_cookie')
            if twitch_cookie:
                twitch_cookie = "--twitch-api-header=Authorization=OAuth " + twitch_cookie
                stream_shell.insert(1, twitch_cookie)
            self.proc = subprocess.Popen(stream_shell)
            self.raw_stream_url = f"http://localhost:{port}"
            i = 0
            while i < 5:
                if not (self.proc.poll() is None):
                    return
                time.sleep(1)
                i += 1
            return True
        with yt_dlp.YoutubeDL() as ydl:
            try:
                info = ydl.extract_info(self.url, download=False)
            except yt_dlp.utils.DownloadError as e:
                logger.warning(self.url, exc_info=e)
                return
            self.raw_stream_url = info['formats'][-1]['url']
            return True

    async def danmaku_download_start(self, filename):
        if self.twitch_danmaku:
            logger.info("开始弹幕录制")
            self.danmaku = DanmakuClient(self.url, filename + "." + self.suffix)
            await self.danmaku.start()

    def close(self):
        if self.twitch_danmaku:
            self.danmaku.stop()
            logger.info("结束弹幕录制")
        try:
            if self.proc is not None:
                self.proc.terminate()
        except:
            logger.exception(f'terminate {self.fname} failed')

    class BatchCheck(BatchCheckBase):
        def __init__(self, urls):
            BatchCheckBase.__init__(self, pattern_id=VALID_URL_BASE, urls=urls)

        def check(self):
            gql = self.get_streamer()
            i = -1
            for data in gql:
                i += 1
                user = data['data'].get('user')
                if not user:
                    continue
                stream = user['stream']
                if not stream:
                    continue
                yield self.usr_dict.get(self.usr_list[i])

        def get_streamer(self):
            ops = []
            for channel_name in self.usr_list:
                op = {
                    'operationName': 'StreamMetadata',
                    'variables': {'channelLogin': channel_name.lower()}
                }
                op['extensions'] = {
                    'persistedQuery': {
                        'version': 1,
                        'sha256Hash': _OPERATION_HASHES[op['operationName']],
                    }
                }
                ops.append(op)
            return get_streamer(ops)


def get_streamer(ops):
    gql = requests.post(
        'https://gql.twitch.tv/gql',
        json=ops,
        headers={
            'Content-Type': 'text/plain;charset=UTF-8',
            'Client-ID': _CLIENT_ID,
        }, timeout=15)
    gql.close()
    return gql.json()

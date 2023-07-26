import logging
import re
import time
from urllib.error import HTTPError

from .engine.decorators import Plugin
from .plugins import general, BatchCheckBase

logger = logging.getLogger('biliup')


def download(fname, url, **kwargs):
    pg = general.__plugin__(fname, url)
    for plugin in Plugin.download_plugins:
        if re.match(plugin.VALID_URL_BASE, url):
            pg = plugin(fname, url)
            for k in pg.__dict__:
                if kwargs.get(k):
                    pg.__dict__[k] = kwargs.get(k)
            break
    return pg.start()


def check_url(plugin, url_status, secs=15):
    try:
        if isinstance(plugin, BatchCheckBase):
            return (yield from plugin.check())
        for url in plugin.url_list:
            # print(f"URL：{url}")
            # print(f"URL_STATUS：{url_status[url]}")
            if url_status[url] == 1:
                logger.debug(f'{url}正在下载中，已跳过检测')
                # print(f"正在下载中，已跳过检测")
                continue
            if plugin(f'检测{url}', url).check_stream():
                yield url
            if url != plugin.url_list[-1]:
                logger.debug('歇息会')
                time.sleep(secs)
    except HTTPError as e:
        logger.error(f'{plugin.__module__} {e.url} => {e}')
    except IOError:
        logger.exception("IOError")
    except:
        logger.exception("Uncaught exception:")

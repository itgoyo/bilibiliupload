import time
import requests
from . import logger
from ..engine.decorators import Plugin
from ..engine.download import DownloadBase


@Plugin.download(regexp=r'(?:https?://)?(?:(?:www)\.)yy\.com')
class YY(DownloadBase):
    def __init__(self, fname, url, suffix='flv'):
        super().__init__(fname, url, suffix)

    def check_stream(self):
        headers = {
            'content-type': 'text/plain;charset=UTF-8',
            'referer': 'https://www.yy.com/',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42'
        }

        if len(self.url.split("www.yy.com/")) < 2:
            logger.debug("直播间地址错误")
            return False
        else:
            rid = self.url.split("www.yy.com/")[1].split('/')[0]

        try:
            millis_13 = int(round(time.time() * 1000))
            millis_10 = int(time.time())
            data = '{"head":{"seq":'+str(millis_13)+',"appidstr":"0","bidstr":"121","cidstr":"'+str(rid)+'","sidstr":"'+str(rid)+'","uid64":0,"client_type":108,"client_ver":"5.11.0-alpha.4","stream_sys_ver":1,"app":"yylive_web","playersdk_ver":"5.11.0-alpha.4","thundersdk_ver":"0","streamsdk_ver":"5.11.0-alpha.4"},"client_attribute":{"client":"web","model":"","cpu":"","graphics_card":"","os":"chrome","osversion":"106.0.0.0","vsdk_version":"","app_identify":"","app_version":"","business":"","width":"1536","height":"864","scale":"","client_type":8,"h265":0},"avp_parameter":{"version":1,"client_type":8,"service_type":0,"imsi":0,"send_time":'+str(millis_10)+',"line_seq":-1,"gear":4,"ssl":1,"stream_format":0}}'
            url = f"https://stream-manager.yy.com/v3/channel/streams?uid=0&cid={rid}&sid={rid}&appid=0&sequence={millis_13}&encode=json"

            result = requests.post(url, timeout=30, headers=headers, data=data).json()
            if 'avp_info_res' in result:
                a = result['avp_info_res']['stream_line_addr']
                self.raw_stream_url = list(a.values())[0]['cdn_info']['url']
                return True
            else:
                logger.debug(f'主播{rid}未开播')
                return False

        except Exception as e:
            logger.error(f"获取直播间信息失败{rid}")
            logger.error(e)
            return False

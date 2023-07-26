import requests

from ..engine.decorators import Plugin
from ..plugins import match1, logger
from ..engine.download import DownloadBase

# VALID_URL_BASE = r"https?://(.*?)\.afreecatv\.com/(?P<username>\w+)(?:/\d+)?"
VALID_URL_BASE = r"https?://play\.afreecatv\.com/(?P<username>\w+)(?:/\d+)?"
STREAM_INFO_URLS = "{rmd}/broad_stream_assign.html"
CHANNEL_API_URL = "http://live.afreecatv.com/afreeca/player_live_api.php"

QUALITIES = ["original", "hd", "sd"]


@Plugin.download(regexp=r"https?://(.*?)\.afreecatv\.com/(?P<username>\w+)(?:/\d+)?")
class AfreecaTV(DownloadBase):
    def __init__(self, fname, url, suffix='flv'):
        super().__init__(fname, url, suffix)

    def check_stream(self):
        logger.debug(self.fname)
        username = match1(self.url, VALID_URL_BASE)
        res_bno = requests.post(CHANNEL_API_URL + "?bjid=" + username,
                                data={"bid": username, "mode": "landing", "player_type": "html5"}, timeout=5)
        res_bno.close()
        if res_bno.json()["CHANNEL"]["RESULT"] == 0:
            return
        try:
            bno = res_bno.json()["CHANNEL"]["BNO"]
            cdn = res_bno.json()["CHANNEL"]["CDN"]
            rmd = res_bno.json()["CHANNEL"]["RMD"]
            res_aid = requests.post(CHANNEL_API_URL, data={
                "bid": username,
                "bno": bno,
                "pwd": "",
                "quality": QUALITIES[0],
                "type": "pwd"
            }, timeout=5)
            res_aid.close()
        except:
            logger.warning(f"afreecaTV {self.url}：获取错误，本次跳过")
            return False
        aid = res_aid.json()["CHANNEL"]["AID"]
        params = {
            "return_type": cdn,
            "broad_key": "{broadcast}-flash-{quality}-hls".format(broadcast=bno, quality=QUALITIES[0])
        }
        res = requests.get(STREAM_INFO_URLS.format(rmd=rmd), params=params, timeout=5)
        res.close()
        self.raw_stream_url = res.json()["view_url"] + "?aid=" + aid
        return True

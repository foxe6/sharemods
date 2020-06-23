import requests
from lxml import html
import mfd


class ShareMods(object):
    def upload(self, file_path: str) -> str:
        url = "https://s2.sharemods.com/cgi-bin/upload.cgi?upload_type=file"
        files = {"file": open(file_path, "rb")}
        r = requests.post(url, files=files)
        return r.json()

    def download(self, url: str, save_dir: str) -> dict:
        data = {
            "op": "download2",
            "id": url.split("/")[-1],
            "rand": "",
            "referer": url,
            "method_free": "Confirm Download",
            "method_premium": ""
        }
        r = requests.post(url, data=data).content.decode()
        r = html.fromstring(r)
        links = r.xpath("//a/@href")
        links = sorted(links, key=lambda x: len(x))
        _mfd = mfd.MFD(save_dir)
        _f = _mfd.download(links[-1])
        _mfd.stop()
        return _f




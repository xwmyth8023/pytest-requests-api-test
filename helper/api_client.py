import requests
from enum import Enum


# class Method(Enum):
#     GET = "GET"
#     POST = "POST"
#     DELETE = "DELETE"
#     PUT = "PUT"
#     OPTIONS = "OPTIONS"
#     HEAD = "HEAD"
#     PATCH = "PATCH"
#

METHODS = ["GET", "POST", "DELETE", "PUT", "OPTIONS", "HEAD", "PATCH"]

class ApiClient():
    SESSION_TOKEN = ""

    def __init__(self):
        self.session = requests.session()

    def update_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def update_cookies(self, cookies):
        if cookies:
            self.session.cookies.update(cookies)

    def send_request(self, url, method, params=None, data=None, json=None, **kwargs):
        if method not in METHODS:
            raise Exception(f"不支持的方法：{method}, 请检查yaml文件里的请求方式是否正确")
        return self.session.request(
            url=url,
            method=method,
            params=params,
            data=data,
            json=json,
            **kwargs
        )

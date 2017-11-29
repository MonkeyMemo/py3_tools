# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Created by Vito on 27/11/2017.
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

__author__ = 'Vito'


class HttpUtils(object):
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def doGet(self, url="", data="", json=""):
        resp = requests.get(url=url, data=data, verify=False)

        pass

    def doPost(self):
        pass

    def __get(self):
        pass

    def __post(self):
        pass

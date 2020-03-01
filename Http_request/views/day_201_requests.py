#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/15 11:07
# @Author: max liu
# @File  : day_201_requests.py

# https://2.python-requests.org//zh_CN/latest/user/quickstart.html

import requests

# get
a = requests.get(url='http://192.168.59.37/Django_app_001/chartjs_from_ajax/chart_Multi_line')
print(a.headers.get('Server'))
print(a.request.headers)
print(a.text)  # 解码后的文本输出
print(a.json())
print(a.content)  # 二进制内容输出byte like
print(a.status_code)
print(a.raise_for_status())
print(a.url)
print(requests.status_codes)

# headers 头字段值不允许有空格
h = """
Host: 192.168.59.37
Connection: keep-alive
Accept: application/json, text/javascript, */*; q=0.01
DNT: 1
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
Referer: http://192.168.59.37/Django_app_001/chartjs_from_ajax
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7
"""
import re

headers = {re.match(r'(.*?):(.*)', k).groups()[0]: re.match(r'(.*?):(.*)', k).groups()[1].strip() for k in
           h.strip().splitlines()}
print(headers)

r = requests.get(url='http://192.168.59.37/Django_app_001/chartjs_from_ajax/chart_Multi_line', headers=headers)

print(r.request.headers)
print(a.json())

# image 处理 钩子函数
from PIL import Image
from io import BytesIO


def images_show(rr, *args, **kwargs):
    i = Image.open(BytesIO(rr.content)) # 从内存读取
    i.show()  # windows可show
    print(rr.url)
    with open('pli-jpg', 'wb') as f:
        f.write(rr.content)


r = requests.get(url='http://192.168.59.37/static/images/d9302fd3cfc19ebbdc7f3d85765437711.jpg', headers=headers, hooks=dict(response=images_show))

# CSR1000V http base认证
from requests.auth import HTTPBasicAuth
r = requests.get(url='http://192.168.59.140//level/15/exec/-/show/ip/http/server/status/CR', headers=headers, auth=HTTPBasicAuth('cisco', 'Cisc0123'))
print(r.text)
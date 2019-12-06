#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/5 22:12
# @Author: max liu
# @File  : index.py

from django.shortcuts import render


def index_go(request):
    title_value = '人生苦短，我用python'
    body_value = '哈哈哈哈啊哈哈哈'
    return render(request, 'index.html', {'return_title': title_value, 'reutrn_body': body_value})

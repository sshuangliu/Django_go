#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/8 21:58
#@Author: max liu
#@File  : db_test_001.py

# 默认Django不允许手动写入数据到DB,通过表单写入
# import django
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_go.settings')
# django.setup()


from Django_app_001.models import Department
import json

# 表结构
# class Department(models.Model):
#     name = models.CharField(max_length=100, blank=False, null=False)
#     summary = models.CharField(max_length=10000, blank=True, null=True)
#     teacher = models.CharField(max_length=100, blank=False)
#     method = models.CharField(max_length=100, blank=False)
#     characteristic = models.CharField(max_length=100, blank=True, null=True)
#     if_provide_lab = models.BooleanField(default=True)
#     detail = models.CharField(max_length=10000, blank=False)


# insert data
depart1 = Department(name='安全',
                     summary='主要讲解网络安全知识',
                     teacher='大爷',
                     method='在线,网真,本地',
                     characteristic='加入黑客技术',
                     if_provide_lab=True,
                     detail=json.dumps(['FW', 'VPN', 'IDS', 'Hacker']))
depart1.save()

depart2 = Department(name='安全',
                     summary='主要讲解网络安全知识',
                     teacher='大叔',
                     method='在线,网真,本地',
                     characteristic='加入黑客技术',
                     if_provide_lab=True,
                     detail=json.dumps(['FW', 'VPN', 'IDS', 'Hacker']))
depart2.save()


depart3 = Department(name='安全',
                     summary='主要讲解网络安全知识',
                     teacher='大婶',
                     method='在线,网真,本地',
                     characteristic='加入黑客技术',
                     if_provide_lab=True,
                     detail=json.dumps(['FW', 'VPN', 'IDS', 'Hacker']))
depart3.save()



# search Data  返回值为一个类，通过其类属性（表列名）获取值
# try:
#     depart = Department.objects.get(teacher='大爷')
#     print(depart.name)
# except Department.DoesNotExist:
#     print('没有找到!')
# except Department.MultipleObjectsReturned:
#     print('找到多个条目!')

# 返回一个可迭代对象,循环 然后通过其属性（表列名）获取值
# departs = Department.objects.filter(teacher='大爷', name='安全')
#
# for depart_obj in departs:
#     print(depart_obj.detail)


# update data
# wir_depart = Department.objects.get(teacher='大叔', name='安全')
# print(wir_depart.summary)
# wir_depart.summary = '主要讲解最新XXOO'
# wir_depart.save()
#



# delete data
# wir_depart = Department.objects.get(teacher='大叔', name='安全')
# wir_depart.delete()

# all_departs = Department.objects.all()
#
# for x in all_departs:
#     print(x)

# Department.objects.all().delete()



#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/31 18:21
# @Author: max liu
# @File  : device_init_ping.py

# 默认Django不允许手动写入数据到DB,通过表单写入
import django
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_go.settings')
django.setup()

from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR
from Django_app_001.models import OPRS_DEVICE_Base
import logging
from kamene.all import *

logging.getLogger("kamene.runtime").setLevel(logging.ERROR)


def ping_momitor():
    for i in OPRS_DEVICE_Base.objects.all():
        nas_ip = i.oprs_device_extension.device_nas_ip
        ping_pkt = IP(dst=nas_ip) / ICMP(type=8, code=0)
        ping_result = sr1(ping_pkt, timeout=2, verbose=False)
        # print('hahhaha')
        # print(i)
        # print(nas_ip)
        # print(ping_pkt.show())
        try:
            if (ping_result[ICMP].type == ping_result[ICMP].code == 0) and (ping_result.getlayer(IP).fields.get(
                    'src') == ping_pkt.getlayer(IP).fields.get('dst')):
                device_ping_result = i.oprs_device_extension
                device_ping_result.device_init = True
                device_ping_result.save()
                print(nas_ip ,'通')
        except TypeError:
            device_ping_result = i.oprs_device_extension
            device_ping_result.device_init = False
            device_ping_result.save()
            print(nas_ip, '不通')

def my_listener(event):
    if event.exception:
        print('任务出错了！！！！！！')
    else:
        print('任务照常运行:周期性监控设备配置变化...5秒一次')


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(func=ping_momitor, args=[], trigger='interval', seconds=5, start_date=datetime.now(), id='interval_task')
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    scheduler._logger = logging

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        exit()

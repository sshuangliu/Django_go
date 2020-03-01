#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/11 22:48
# @Author: max liu
# @File  : ajax_json_rpc.py

from django.http import JsonResponse
# from Django_app_001.models import CPU_memory_utli
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# @permission_required('Django_app_001.view_cpu_memory_utli')
# @login_required()
def chartjs_ajax_json(request, chart_type):
    if chart_type == 'chart_Multi_line':
        items = CPU_memory_utli.objects.filter(device_ip='172.1.1.1')
        labelname = ['CPU利用率', 'Memory利用率']
        cpu_values = []
        memory_values = []
        device_name_list = []
        device_ip_list = []
        monitor_time = []
        for item in items:
            device_name_list.append(item.device_name)
            device_ip_list.append(item.device_ip)
            cpu_values.append(item.cpu_utli)
            memory_values.append(item.memory_utli)
            monitor_time.append(item.create_date.strftime("%Y-%m-%d %H:%M:%S"))

        return JsonResponse({'labelname': labelname,
                             'x_values': monitor_time,
                             'y_values': [cpu_values, memory_values],
                             'title': device_name_list[0] + '/' + device_ip_list[0]})

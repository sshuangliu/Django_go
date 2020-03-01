#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/9 13:12
# @Author: max liu
# @File  : urls.py


from django.urls import path, include
from Django_app_001.views.views_app_001 import device_add, device_select, device_del, device_update, \
    chartjs_from_django, chartjs_from_ajax, echarts_from_django, echarts_from_ajax
from Django_app_001.views.ajax_json_rpc import chartjs_ajax_json

urlpatterns = [

    path('device_add', device_add),
    path('device_select', device_select),
    path('device_del/<int:device_id>', device_del),
    path('device_update/<int:device_id>', device_update),
    path('chartjs_from_django', chartjs_from_django),
    path('chartjs_from_ajax', chartjs_from_ajax),
    path('chartjs_from_ajax/<str:chart_type>', chartjs_ajax_json),  # json_rpc
    path('echarts_from_django', echarts_from_django),
    path('echarts_from_ajax', echarts_from_ajax)

]

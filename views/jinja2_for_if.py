#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/12/9 12:26
#@Author: max liu
#@File  : jinja2_for_if.py

from django.shortcuts import render
from datetime import datetime
from data import courses_db
from db.models import Courses
import json
from django.contrib.auth.decorators import login_required


def summary_def(request):
    # mytime = int(datetime.now().strftime("%w"))
    mytime = int(datetime.strptime('2019-04-14', '%Y-%m-%d').strftime("%w"))
    summary_title = '課程摘要Title'
    summary = '課程摘要Body'
    # courses_list = ['安全', 'Python', 'DC']
    courses_list = []
    teacher_list = []
    courses_result = Courses.objects.all()
    for x in courses_result:
        courses_list.append(x.courses_name)
        teacher_list.append({'courses': x.courses_name, 'teacher': x.courses_teacher})

    # teacher_list = [{'courses': '安全', 'teacher': '1'},
    #                 {'courses': '数据中心', 'teacher': '2'},
    #                 {'courses': '路由交换', 'teacher': '3'},
    #                 {'courses': 'VIP', 'teacher': '4'},
    #                 ]

    return render(request, 'summary.html', locals())


@login_required()
def sec_course(request):
    c = Courses.objects.get(courses_name='安全')
    courses_sec = {'方向': c.courses_name,
                   '摘要': c.courses_summary,
                   '授课老师': c.courses_teacher,
                   '授课方式': c.courses_method,
                   '课程特色': c.courses_characteristic,
                   '试验环境': c.courses_provide_lab,
                   '具体课程': json.loads(c.courses_detail)}
    return render(request, 'course.html', {'courseinfo': courses_sec})


@login_required()
def dc_course(request):
    c = Courses.objects.get(courses_name='数据中心')
    courses_dc = {'方向': c.courses_name,
                  '摘要': c.courses_summary,
                  '授课老师': c.courses_teacher,
                  '授课方式': c.courses_method,
                  '课程特色': c.courses_characteristic,
                  '试验环境': c.courses_provide_lab,
                  '具体课程': json.loads(c.courses_detail)}
    return render(request, 'course.html', {'courseinfo': courses_dc})
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/12 12:45
# @Author: max liu
# @File  : app_001_login.py

from django.shortcuts import render
from Django_app_001.forms import UserForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout


def app_001_login(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            next_url = request.GET.get('next', '/')
            return HttpResponseRedirect(next_url)

        else:
            return render(request, 'registration/app_001_login.html', {'form': form, 'error': '用户名或密码错误'})
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')

        else:
            form = UserForm()
            return render(request, 'registration/app_001_login.html', {'form': form})


def app_001_logout(request):
    logout(request)
    return HttpResponseRedirect('/accounts/login')
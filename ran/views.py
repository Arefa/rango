# -*-coding: utf-8 -*-
# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context_dict = {'boldmessage': '这里是boldmessage'}
    return render(request, 'ran/index.html', context_dict)
    # return HttpResponse('欢迎啊!<br/><a href="/ran/about">关于</a>')


def about(request):
    context_dict = {'about': '这里是about'}
    return render(request, 'ran/about.html', context_dict)
    # return HttpResponse('关于页面<br/><a href="/ran/">主页</a>')

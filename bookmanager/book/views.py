from django.shortcuts import render

# Create your views here.
"""
所谓视图 就是一个python函数
视图函数有两个要求：
1.视图函数的第一个参数是接收请求，这个请求就是HttpRequest的类对象
2.必须返回一个响应
"""
from django.http import HttpRequest
from django.http import HttpResponse


def index(request):

    return HttpResponse('OK')

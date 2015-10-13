#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

import json
# Create your views here.

def index(request):
    return HttpResponse(u"欢迎光临")

def home(request):
    string = "用它来建网站"
    return render(request,'home.html',{'string':string})

def list(request):
    list = ['HTML','CSS','jquery']
    return render(request,'list.html',{'list':list})
def dict(request):
    info_dict = {'site':'自强学堂','content':'各种IT技术教程'}
    return render(request,'dict.html',{'info_dict':info_dict})

def json_list(request):
    list = ['自强学堂','json ceshi']
    dict = {'site':'自强学堂','author':'涂中卫'}

    return render(request,'json.html',{
            'list':json.dumps(list),
            'dict':json.dumps(dict)
            })
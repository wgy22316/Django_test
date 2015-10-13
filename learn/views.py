#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse(u"欢迎光临")

def home(request):
    string = "用它来建网站"
    return render(request,'home.html',{'string':string})

def list(request):
    list = ['HTML','CSS','jquery']
    return render(request,'list.html',{'list':list})
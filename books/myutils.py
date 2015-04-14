#-*- coding:utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from books.models import *
from datetime import *
import re
import random
import json
import xml
import urllib

def state(n):
    return {"state":n}

#decorator 
#check if the request is post
def check_request(fn):
    def wrapper(request):
        if request.method != "POST":
            print "error"
            return HttpResponse(json.dumps(state(1)),content_type = "application/json")
        return fn(request)
    return wrapper


def JsonReturn(a):
    return HttpResponse(a,content_type = "application/json")


def add_a_book(isbn):
    if not BookInfo.objects.filter(isbn=isbn):
        b = BookInfo(isbn = isbn)
        b.save()
    return JsonReturn(json.dumps(state(0)))

##crawl douban api
def update_data_using_douban_api(book):
    if not book.has_data:
        data = urllib.urlopen("http://api.douban.com/book/subject/isbn/"+book.isbn).read()

##to be continued


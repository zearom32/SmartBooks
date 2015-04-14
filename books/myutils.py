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
def parse_book_json(data,s):
    return data.get(s).encode('utf-8')

def update_data_using_douban_api(book):
    print "start"
    data = urllib.urlopen("https://api.douban.com/v2/book/isbn/"+book.isbn).read()
    data = json.loads(data)
    book.pic_url = data.get('images').get('large').encode('utf-8')
    book.title = parse_book_json(data,'title')
    book.pages = int(parse_book_json(data,'pages').replace('页',""))
    authors = ""
    for a in data.get('author'):
        authors = authors + a.encode('utf-8')+','
    book.author = authors
    print book.author
    book.price = parse_book_json(data,'price')
    book.publisher = parse_book_json(data,'publisher')
    book.pubdate = parse_book_json(data,'pubdate')
    book.has_data = True
    book.doubanid = parse_book_json(data,'id')
    book.save()
##to be continued


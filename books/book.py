from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.forms.models import model_to_dict
from django.core import serializers
from books.models import *
from datetime import *
import re
import random
import json
from myutils import *

def bookinfo(request):
    body = json.loads(request.body)
    book = BookInfo.objects.filter(isbn = body['isbn']) 
    if not book:
        return JsonReturn(json.dumps(state(1)))
    book = book[0]
    book = model_to_dict(book)
    book['state'] = 0
    bookjson = json.dumps(book)
    return JsonReturn(bookjson)

##support search by name
def search_book(request):
    body = json.loads(request.body)
    keywords = body['book_name']
    return JsonReturn(json.dumps(search_book_by_keywords(keywords)))

@check_request
def homepage(request):
    ans = state(0)
    body = json.loads(request.body)
    st = int(body['start_book_no'])
    ed = int(body['end_book_no'])
    num = ed - st + 1
    book = BookInfo.objects.all()[max(0,st-1):ed]
    b  =  []
    for i,item in enumerate(book):
        m = dict()
        m['book_no'] = i + st
        m['isbn']  = item.isbn
        b.append(m)
    ans['books'] = b
    return JsonReturn(json.dumps(ans))


#####################private functions############
def search_book_by_keywords(keywords):
    books = BookInfo.objects.filter(title__icontains=keywords)
    ans = dict()
    if not books:
        ans['state'] = 1
        return ans
    ans['state'] = 0
    b = []
    for book in books:
        bookmap = dict()
        bookmap['isbn'] = book.isbn
        b.append(bookmap)
    ans['books'] = b
    return ans


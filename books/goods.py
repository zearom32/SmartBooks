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
from myutils import *

def books_of_a_seller(request):
    body = json.loads(request.body)
    seller = User.objects.filter(username = body['seller'])
    if not seller:
        return JsonReturn(json.dumps(state(0)))
    books =  seller.goods.all()
    if not books:
        return JsonReturn(json.dumps(state(0)))
    ans = dict()
    ans['state'] = 0
    book = []
    for b in books:
        w = dict()
        w['isbn'] = b.isbn
        book.append(w)
    ans['books'] = book
    return JsonReturn(json.dumps(ans))
        
        

def goodsinfo(request):
    pass

def sellers_of_a_book(request):
    body = json.loads(request.body)
    isbn = body.get('isbn')
    if not isbn:
        return JsonReturn(json.dumps(state(0)))
    book = BookInfo.objects.filter(isbn = isbn)
    if not book:
        return JsonReturn(json.dumps(state(0)))
    users = books.goods.all()
    if not users:
        return JsonReturn(json.dumps(state(0)))
    ans = []
    ans['state'] = 0
    
    user = []
    for u in users:
        m = dict()
        m['seller'] = u.username
        user.append(m)
    ans['sellers'] = m
    return JsonReturn(json.dumps(ans))



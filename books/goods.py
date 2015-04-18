from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from django.forms.models import model_to_dict
from books.models import *
from datetime import *
import re
import random
import json
from myutils import *

def books_of_a_seller(request):
    body = json.loads(request.body)
    seller = body.get('seller')
    goods = GoodsInfo.objects.filter(seller__username = seller)
    if not goods:
        return JsonReturn(json.dumps(state(0)))
    ans = dict()
    ans['state'] = 0
    book = []
    for g in goods:
        b = g.book
        w = dict()
        w['isbn'] = b.isbn
        book.append(w)
    ans['books'] = book
    return JsonReturn(json.dumps(ans))
        
        

def goodsinfo(request):
    body = json.loads(request.body)
    isbn = body.get('isbn')
    username = body.get('username')
    if not isbn or not username:
        return JsonReturn(json.dumps(state(0)))
    goods = GoodsInfo.objects.filter(seller__usrname = username, book__isbn = isbn)
    if not goods:
        return JsonReturn(json.dumps(state(0)))
    goods = goods[0]
    ans = model_to_dict(goods)
    ans['state'] = 0
    return JsonReturn(json.dumps(ans))
    


def sellers_of_a_book(request):
    body = json.loads(request.body)
    isbn = body.get('isbn')
    goods = GoodsInfo.objects.filter(book__isbn = isbn)
    for g in GoodsInfo.objects.all():
        print g.book.isbn
    print goods
    if not goods:
        return JsonReturn(json.dumps(state(0)))
    ans = dict()
    ans['state'] = 0
    
    user = []
    for k in goods:
        u = k.seller
        m = dict()
        m['seller'] = u.username
        user.append(m)
    ans['sellers'] = user
    return JsonReturn(json.dumps(ans))



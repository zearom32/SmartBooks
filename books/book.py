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

def bookinfo(request):
    pass

def search_book(request):
    pass

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



###############################################
##private function#############################
##############


def add_a_book(isbn):
    if not BookInfo.objects.filter(isbn=isbn):
        b = BookInfo(isbn = isbn)
        b.save()
    return JsonReturn(json.dumps(state(0)))



def crawl_data(request):
    pass

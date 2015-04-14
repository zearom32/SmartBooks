from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
from books.models import *
from datetime import *
from myutils import *
import re
import random
import json
import time
def addbooks(request):
    print request.body
    body = json.loads(request.body)
    isbn = body.get('isbn')
    print isbn
    for item in isbn:
        add_a_book(item)

    return JsonReturn(json.dumps(state(0)))


def updatebooks(request):
    body = json.loads(request.body)
    if body['username'] == "zearom32":
        all_books = BookInfo.objects.filter(has_data=False)
        if body.has_key('all'):
            all_books = BookInfo.objects.all()
        for book in all_books:
            update_data_using_douban_api(book)
            time.sleep(8)
    return JsonReturn(json.dumps(state(0)))

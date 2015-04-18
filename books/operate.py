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
import urllib

def buy(request):
    pass

##just use it as a test
@check_request
def sell(request):
    a = json.loads(request.body)
    print a
    print a['books'][1]['b']
    ans = dict()
    ans['state'] = 0
    return HttpResponse(json.dumps(ans),content_type="application/json")


def douban_request_test(request):
    page = urllib.urlopen("http://book.douban.com/subject/26299926/").read()
    return HttpResponse(page,content_type = "text")

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from books.models import *
from datetime import *
import re
import random
import json
from myutils import *

PKU_MAIL = r'@pku.edu.cn'
#a simple register
#need to virify the username using the pku mail
@check_request
def register(request):
    body = json.loads(request.body) 
    if User.objects.filter(username=body['username']):
        return JsonReturn(json.dumps(state(2)))
    user = User.objects.create_user(body['username'],body['username']+PKU_MAIL,body['password'])
    user.save()
    return JsonReturn(json.dumps(state(0)))

@check_request
def Login(request):
    body = json.loads(request.body)
    user = authenticate(username = body['username'],password=body['password'])
    if user is not None:
        if user.is_active:
            return JsonReturn(json.dumps(state(0)))
    return JsonReturn(json.dumps(state(1)))

@check_request
def sellerinfo(request):
    pass

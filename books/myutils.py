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

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

def addbooks(request):
    print request.body
    body = json.loads(request.body)
    isbn = body.get('isbn')
    print isbn
    for item in isbn:
        add_a_book(item)

    return JsonReturn(json.dumps(state(0)))

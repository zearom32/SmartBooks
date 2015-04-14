from django.shortcuts import render
from django.http import HttpResponse
from users import *
from book import *
from goods import *
from operate import *
from dev import *
# Create your views here.


def index(request):
    return HttpResponse("Hello World!")

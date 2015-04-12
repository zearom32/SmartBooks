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


def books_of_a_seller(request):
    pass

def goodsinfo(request):
    pass

def sellers_of_a_book(request):
    pass


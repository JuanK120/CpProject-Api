import json
from django.shortcuts import render
from django.http import HttpResponse
from json import *

# Create your views here.

def test(request):
    ret = """<html><body><strong>this is a test!!</strong></body></html>""" 
    return HttpResponse(ret)
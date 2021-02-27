from django.shortcuts import render

from .methods.page import __page

# Create your views here.

def page(request):
    #print(request)
    return __page(request)
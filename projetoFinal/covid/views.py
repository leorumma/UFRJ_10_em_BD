from django.shortcuts import render

from .methods.page import __page

# Create your views here.

def page(request):
    return __page()

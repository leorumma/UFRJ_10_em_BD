from django.shortcuts import render

from .methods.test import test_query

# Create your views here.

def test_page(request):
    return test_query()

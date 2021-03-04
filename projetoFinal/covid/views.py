from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .methods.page import __page

# Create your views here.

# Detalhes do objeto request:
# https://docs.djangoproject.com/en/3.1/ref/request-response/

def page(request):
    output = {
	    "title": "Covid Graphs",
	    "headers": [], # espaco para cards se for usar
	    "content": [{
            "title": "Test Graphs",
		    "children": [__page(request.path, request.GET)],
        }],
    }
    #print(request)
    print(request.GET)
    return JsonResponse(output)

def main_page(request):
    if 'simulated' in request.GET and request.GET['simulated'] in ('0', '0/'):
        children = [
                __page('/answers/'),
                __page('/timeline/'),
                __page('/sodium/'),
                __page('/o2byco2/'),
                ]
    else:
        children = [
                __page('/age_groups/'),
                __page('/outcomes/'),
                __page('/age_group_outcomes/'),
                __page('/age_group_sexes/'),
                ]

    response = {
        'title': 'Main Page',
        "headers": [], # espaco para cards se for usar
        'content': [{
            "title": "Covid Graphs",
            "children": children,
            },
        ],
    }
    return JsonResponse(response)
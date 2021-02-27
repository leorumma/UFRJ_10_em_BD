from django.http import JsonResponse, HttpResponse

from covid.methods.test import test_query

def __page():

	output = {
	    "title": "Covid Graphs",
	    "headers": [], # espaco para cards se for usar
	    "content": [{
            "title": "Test Graphs",
		    "children": [{
			    # teste
			    "title": "teste title",
			    "subtitle": "teste subtitle",
			    "description": "teste description",
			    "type": "test type",
			    "content": test_query(),
		    }],
        }],
    }

	return JsonResponse(output)

from django.http import JsonResponse, HttpResponse

from covid.methods.test import test_query
from . import age_groups

methods = {
	"/teste/" : test_query,
	"/age_groups/": age_groups.do_query
}

def __page(request):

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
			    "content": methods[request.path](),
		    }],
        }],
    }

	return JsonResponse(output)

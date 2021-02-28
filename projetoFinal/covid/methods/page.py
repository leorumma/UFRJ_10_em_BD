from django.http import JsonResponse, HttpResponse

from covid.methods.test import test_query
from . import age_groups
from . import outcomes


from collections import defaultdict

#TODO: melhorar isso aqui, fazer uma classe em vez de vários dicts
methods = {
	"/teste/" : test_query,
	"/age_groups/": age_groups.do_query,
	"/outcomes/": outcomes.do_query,
}

titles = defaultdict(lambda : "Test Title", {
	"/age_groups/": "Faixa Etária dos Pacientes",
	"/outcomes/": "Sumário dos Desfechos",
})

types = defaultdict(lambda : "pie", {

})

def __page(path, queryargs={}):

	output = {
		# teste
		"title": titles[path],
		"subtitle": "teste subtitle",
		"description": "teste description",
		"type": types[path],
		"content": methods[path](**queryargs),
    }

	return output

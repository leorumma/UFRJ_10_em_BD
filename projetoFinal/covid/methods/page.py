from django.http import JsonResponse, HttpResponse

from covid.methods.test import test_query
from . import age_groups
from . import age_group_outcomes
from . import age_group_sexes
from . import outcomes


from collections import defaultdict

#TODO: melhorar isso aqui, fazer uma classe em vez de vários dicts
methods = {
	"/teste/" : test_query,
	"/age_groups/": age_groups.do_query,
	"/outcomes/": outcomes.do_query,
	"/age_group_outcomes/": age_group_outcomes.do_query,
	"/age_group_sexes/": age_group_sexes.do_query,
}

titles = defaultdict(lambda : "Test Title", {
	"/age_groups/": "Faixa Etária dos Pacientes",
	"/outcomes/": "Sumário dos Desfechos",
	"/age_group_outcomes/" : "Desfechos por Faixa Etária",
	"/age_group_sexes/": "Sexo por Faixa Etária",
})

types = defaultdict(lambda : "pie", {
	"/age_group_outcomes/": "stacked bar",
	"/age_group_sexes/": "stacked bar",
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

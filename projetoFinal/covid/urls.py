from django.urls import path
from .views import *

urlpatterns = [
	path('teste/', page, name='page'),
	path('age_groups/', page, name='page'),
	path('outcomes/', page, name='page'),
	path('age_group_outcomes/', page, name='page'),
	path('age_group_sexes/', page, name='page'),

	path('answers/', page, name='page'),
	path('timeline/', page, name='page'),
	path('sodium/', page, name='page'),
	path('o2byco2/', page, name='page'),
	
	path('mainpage/', main_page, name='Main Page'),
]

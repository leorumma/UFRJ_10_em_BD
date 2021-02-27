from django.urls import path
from .views import *

urlpatterns = [
	path('teste/', page, name='page'),
	path('age_groups/', page, name='page'),
	path('outcomes/', page, name='page'),
]

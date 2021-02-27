from django.urls import path
from .views import *

urlpatterns = [
	path('teste/', test_page, name='test_page'),
]

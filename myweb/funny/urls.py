from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
	path('', views.hello, name='hello'),
    path('cv/', views.results, name='resume'),
]

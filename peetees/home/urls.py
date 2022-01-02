from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home import views

urlpatterns = [
	path("", views.home),
    path('grocery/', views.grocery),
	path('bakery/', views.bakery),
	path('dairy/', views.dairy),
	path('stationary/', views.stationary),
	path('electrical/', views.electrical),
	path('fruits/', views.fruits),
	path('vegetables/', views.vegetables)
]

from django.contrib import admin
from django.urls import path, include
from .views import index, about, contacts

urlpatterns = [   
    path('', index),
    path('about', about),
    path('contacts', contacts),
]
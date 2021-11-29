from django.shortcuts import render
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home,name='blog-home'),  #views function mapper to the home fn which returns the http res
    path('about/', views.about,name='blog-about'),
]

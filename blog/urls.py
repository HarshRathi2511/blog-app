from django.shortcuts import render
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.PostListView.as_view(),name='blog-home'),  #views function mapper to the home fn which returns the http res
    path('about/', views.about,name='blog-about'),
    path('post/<int:pk>', views.PostDetailView.as_view(),name='post-detail'), 
    #to create the custom urls as per the blogs
]

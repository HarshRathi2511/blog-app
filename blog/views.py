from typing import List
from django.db.models import fields
from django.shortcuts import render  # to return a render template
from .models import Post
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from  django.contrib.auth.mixins import LoginRequiredMixin
from blog import models

# function based views


def home(request):  # function
    context = {
        'posts': Post.objects.all()
        # the 'posts' key is gonna be accessible within the home.html page
    }
    return render(request, 'blog/home.html', context)

# class based view


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # the list will look here
    context_object_name = 'posts'  # what it will be accesed as in the frontend
    ordering = ['-date_posted']


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class PostDetailView(DetailView):
    model = Post
    # template naming convention :- <app>/<model>_<viewtype>.html
    # template_name = 'blog/home.html'    #the list will look here
    # context_object_name = 'posts'   #what it will be accesed as in the frontend

# LoginRequiredMixin otherwise we will get redirected to the login required mixin 
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields=['title','content']

    #overriding the form valid method to specify the author of the blog 
    def form_valid(self,form) :
        form.instance.author =self.request.user
        return super().form_valid(form)

    #after creating the post we need to redirect to the detail page of the post view 
    # we need to create a method in the model that returns the url of each specefic instance  


# Class based views 
# List view eg- List of videos in utube
# Detail View 
# Class view
# Update view  
# Delete view 
  


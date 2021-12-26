from typing import List
from django.db.models import fields
from django.shortcuts import render  # to return a render template
from .models import Post
from django.views.generic import ListView, DetailView, DeleteView, CreateView,UpdateView
from  django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from blog import models


# function based views


def home(request):  # function
    context = {
        'posts': Post.objects.all()
        # the 'posts' key is gonna be accessible within the home.html page
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})    

# Class based views 
# List view eg- List of videos in utube
# Detail View 
# Class view
# Update view  
# Delete view 


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # the list will look here
    context_object_name = 'posts'  # what it will be accesed as in the frontend
    ordering = ['-date_posted']




class PostDetailView(DetailView):
    model = Post
    # template naming convention :- <app>/<model>_<viewtype>.html
    # template_name = 'blog/home.html'    #the list will look here
    # context_object_name = 'posts'   #what it will be accesed as in the frontend

# LoginRequiredMixin otherwise we will get redirected to the login required mixin 
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']

    #overriding the form valid method to specify the author of the blog before creating the form 
    def form_valid(self,form) :
        form.instance.author =self.request.user
        return super().form_valid(form)

    #after creating the post we need to redirect to the detail page of the post view 
    # we need to create a method in the model that returns the url of each specefic instance  

# for only the author to update the views 
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields=['title','content']

    #overriding the form valid method to specify the author of the blog 
    def form_valid(self,form) :  #(method) form_valid: (self: Self@PostUpdateView, form) -> HttpResponse
        form.instance.author =self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object() #Return the object the view is displaying.  
        if self.request.user ==post.author:
            return True
        return False    

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object() #Return the object the view is displaying.  
        if self.request.user ==post.author:
            return True
        return False           

  


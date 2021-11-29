from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# handle the traffic from the homepage of the blog
def home(request):   #function
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')    


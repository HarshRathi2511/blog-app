from django.shortcuts import render  #to return a render template 
from .models import Post 

# handle the traffic from the homepage of the blog
def home(request):   #function
    context = {
        'posts':Post.objects.all()
        # the 'posts' key is gonna be accessible within the home.html page 
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})    


from django.shortcuts import render  #to return a render template 

posts = [  #dictionary 
    {
        'author':'Harsh Rathi',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted':'August 27 ,2018'
    },
    {
        'author':'Kinjal Shah',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted':'August 27 ,2018'
    }
    
]

# handle the traffic from the homepage of the blog
def home(request):   #function
    context = {
        'posts':posts
        # the 'posts' key is gonna be accessible within the home.html page 
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')    


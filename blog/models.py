# Create your models here.
from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User  #to import the user models 
from django.urls import reverse

# (class) User
# Users within the Django authentication system are represented by this model.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    #CASCADE when a user is deleted the post also gets deleted
    #post can have only one user,whereas one user can have multiple posts 

    def __str__(self) :  #magic/spell methods 
        return self.title   #Return str(self).

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})  
# pk -> primary key 
# reversed returns the full path as the string 
# The **kwargs argument is a dictionary argument, kwargs is the abbreviation of key word arguments. 
# It means all the function keyword value pair arguments can be accessed use kwargs as a dictionary.
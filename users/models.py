from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.files import ImageField

# to create the profile model 
class Profile(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE)  
  image = models.ImageField(default='default.jpg',upload_to ='profile_pics')

  def __str__(self) :
      return f'{self.user.username}\'s Profile'
    
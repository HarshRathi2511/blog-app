from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User  #interaction with this model 
        fields=['username','email','password1','password2']
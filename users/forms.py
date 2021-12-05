from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model=User  #interaction with this model 
        fields=['username','email','password1','password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()  #additional fields to be added apart from the built in user model 

    class Meta:
        model=User  #interaction with this model 
        fields=['username','email']


class ProfileUpdateForm(forms.ModelForm)  :
    # Think of the Meta class as a container for configuration attributes of the outer class.
    # As new instances of your outer class are created, the class constructor will look to
    #  the Meta attribute for specific configuration details
    class Meta:
        model= Profile 
        fields=['image']   


        
           
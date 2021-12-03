
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from users.forms import UserRegistrationForm

# Create your views here.
def register(request):
    #to have the django created form
     
    if request.method =='POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid() :    
          returnedUser= form.save() #save the user
          print('$$$$$$$$') 
          print(returnedUser)
          username = form.cleaned_data.get('username')
          messages.success(request,f'Your account has been created ,Please login {returnedUser.username}!') #to show a snackbar 
          # redirect them to the login page after creating the account
          return redirect('login')
    else :
      form =UserRegistrationForm()

    return render(request,'users/register.html',{'form':form})

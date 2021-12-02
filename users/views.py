
from django.contrib.auth import forms
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
          form.save() #save the user 
          username = form.cleaned_data.get('username')
          messages.success(request,f'Account created for {username}!') #to show a snackbar 
          return redirect('blog-home')
    else :
      form =UserRegistrationForm()

    return render(request,'users/register.html',{'form':form})


from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from users.forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# Create your views here.


def register(request):
    # to have the django created form
    #

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
          returnedUser = form.save()  # save the user
          print('$$$$$$$$')
          print(returnedUser)
          username = form.cleaned_data.get('username')
          # to show a snackbar
          messages.success(
              request, f'Your account has been created ,Please login {returnedUser.username}!')
          # redirect them to the login page after creating the account
          return redirect('login')
    else:
      form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required  # for a logged in user to only see the profile
# Decorators are a very powerful and useful tool in Python
# since it allows programmers to modify the behaviour of function or class.
def profile(request):
  # when a profile returns data from the post request then it is accesed in the same view using the request.Methof

     if request.method == 'POST':
      #  instances to know what profiles to update 
          u_form = UserUpdateForm(request.POST,instance=request.user)
          p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

          if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(
              request, f'Your account has been updated ')
          # redirect them to the profile page after creating the account
            return redirect('profile')

     else: 
           u_form = UserUpdateForm(instance=request.user)
           p_form = ProfileUpdateForm(instance=request.user.profile)

     context = {
      'u_form':u_form,
      'p_form':p_form,
     }
     return render(request,'users/profile.html',context) 

 # http://127.0.0.1:8000/login/?next=/profile/  => next page redirected is the profile    


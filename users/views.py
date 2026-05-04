from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import ExtendUserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
           
            user = form.get_user()
            login(request, user)
            request.session['access_fuc'] = True
            print("Login success")
            return redirect('/app/list-department')
        
        else:
            print("Form Invalid", form.errors)
    else:
        form = AuthenticationForm()
    context = {'form':form}
    return render(request, 'login.html', context)

def register_user(request):
    if request.method == "POST":
        form = ExtendUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The Signup Success")
            return redirect('login-user')
    else:
        
        form = ExtendUserCreationForm()
    context = {'form' : form}
    return render(request, 'signup.html', context)
    
    
def logout_user(request):
    logout(request)
    messages.info(request, "You are successfully Logout")
    return redirect('users:login-user')
    
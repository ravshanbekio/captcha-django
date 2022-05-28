from django.shortcuts import render, redirect
from .forms import RegisterUserForm
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            return redirect('home')
        
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form':form})

def login_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'login.html', {'form':form})

def logout_user(request):
    logout(request)

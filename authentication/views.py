from django.contrib.auth import logout
from django.shortcuts import render, redirect


# Create your views here.

def login_user (request):
    return render(request, 'auth/login.html')

def account (request):
    return render(request, 'auth/account.html')

def logout_user (request):
    logout(request)
    return redirect('index')
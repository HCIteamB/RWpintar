from django.contrib.auth import authenticate, login, get_user_model
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url

from .forms import LoginForm, RegisterForm

def login(request):
    if request.method == 'POST':
    # for login
        messages.error(request, 'tert')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        nik = request.POST['nik']
        password = request.POST['password']
        password2 = request.POST['password2']
        return
    else:
        return render(request, 'signin.html')

def register(request):
    if request.method == 'POST':
    # for register
        return
    else:
        return render(request, 'signup.html')

def tetis(request):
    return render(request, 'signup-next.html')

def logout(request):
    return redirect('home.html')

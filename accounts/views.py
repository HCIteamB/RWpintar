from django.contrib.auth import authenticate, login, get_user_model
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import logout as auth_logout
from django.views.generic import CreateView, FormView
from django.http import HttpResponse
from django.contrib import messages, auth
from django.shortcuts import render,redirect
from django.contrib import messages
from django.conf import settings
from django.utils.http import is_safe_url

from .forms import  RegisterForm, LoginForm, biodata
from .models import Acc

User = get_user_model()

def register(request):
    form = RegisterForm(request.POST or None)
    context={
            'form': form
            }
    template = 'signup.html'

    if form.is_valid():
        form.save()
        messages.success(request, "pendaftaran sukses")
    else:
        messages.error(request, "pendaftaran gagal")
    return render(request, "signup.html", context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email , password=password)

        if user is not None:
            auth.login(request, user)
            print('login')
            return redirect("/")
        else:
            messages.error(request, "anda salah memasukkan akun atau akun tidak ada")
            return redirect('signin')

    return render(request, "signin.html")

def logout(request):
    auth.logout(request)
    messages.success(request, "anda berhasil keluar")
    return redirect('/')


def warga(request):
    wargas = Acc.objects.order_by('first_name')

    paginator = Paginator(wargas, 20)
    page = request.GET.get('page')
    paged_lists = paginator.get_page(page)
    context={
            'wargas': paged_lists
            }
    return render(request, 'warga.html', context)


def setting(request):
    return render(request, 'settings.html')

def biodata(request):
    if request.method == "POST":  
        form = biodata(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('home')  
            except:  
                pass  
    else:  
        form = biodata(request.POST)  
    return render(request,'signup-next.html',{'form':form})  

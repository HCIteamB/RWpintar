from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('signin/', views.login , name='login'), 
    path('signup/', views.register, name='register'),
    path('warga/', views.warga, name='warga'),
    path('biodata/', views.biodata, name='biodata'),
    path('settings/', views.setting, name='setting'),
    path('logout/', views.logout, name='logout')
        ]

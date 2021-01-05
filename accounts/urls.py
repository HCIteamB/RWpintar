from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.login, name='login'), 
    path('signup/', views.register, name='register'),
    path('signup-next/', views.tetis, name='signup-next')
        ]

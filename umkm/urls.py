from django.urls import path
from . import views

urlpatterns = [
    path('', views.umkm, name='umkm-list'), 
    path('<int:umkm_id>', views.umkm, name='umkm-views')
        ]

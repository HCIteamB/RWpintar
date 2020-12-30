from django.urls import path
from . import views

urlpatterns = [
    path('<int:umkm_id>', views.umkm, name='umkm-views')
        ]

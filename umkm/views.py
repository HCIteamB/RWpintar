from django.shortcuts import render
from .models import umkm

def umkm(request):
    Umkm = umkm.objects.all()
    return render(request, "umkm.html")

def umkm_views(request):
    return render(request, "umkm-detail.html")

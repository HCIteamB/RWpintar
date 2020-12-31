from django.shortcuts import render

def umkm(request):
    return render(request, "umkm.html")

def umkm_views(request):
    return render(request, "umkm-detail.html")

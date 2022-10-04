from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"stok/index.html")

def stoks(request):
    return render(request,"stok/stoks.html")

def stok_details(request,id):
    return render(request,"stok/stok_details.html",{
        "id":id
    })

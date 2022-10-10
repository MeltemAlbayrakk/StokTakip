from re import S
from django.http.response import HttpResponse
from django.shortcuts import render
from stok.models import Category, Stok


# Create your views here.

def index(request):
    context ={
        "stoks": Stok.objects.filter(is_active=True,is_home=True),
        "categories": Category.objects.all()
    }
    return render(request,"stok/index.html",context)

def stoks(request):
    context ={
        "stoks":Stok.objects.filter(is_active=True),
        "categories": Category.objects.all()
    }
    return render(request,"stok/stoks.html",context)

def stok_details(request,slug):

    stok=Stok.objects.get(slug=slug)
    return render(request,"stok/stok_details.html",{
        "stok": stok
    })

def stoks_by_category(request, slug):
    pass

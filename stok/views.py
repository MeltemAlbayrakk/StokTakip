from unicodedata import category
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from stok.forms import StokForm, StokForm2
from stok.models import Bolum, Category, Cihaz
from datetime import datetime
from django.db.models import Q


# Create your views here.

def index(request):
    context ={
        "stoks":Cihaz.objects.filter(Q(status="servis") | Q(status="bekleme")),
        "categories": Category.objects.all()
    }
    return render(request,"stok/index.html",context)

def stoks(request):
    context ={
        "stoks":Cihaz.objects.filter(),
        "categories": Category.objects.all()
    }
    return render(request,"stok/stoks.html",context)

def stok_details(request,slug):

    stok=Cihaz.objects.get(slug=slug)
    return render(request,"stok/stok_details.html",{
        "stok": stok
    })

def stoks_by_category(request, slug):
    context ={
        "stoks": Cihaz.objects.filter(category__slug=slug),        
        "categories": Category.objects.all(),
        "selected_category": slug
    }
    return render(request,"stok/stoks.html",context)


def cihaz_ekle(request):

    if request.method == 'POST':
        form = StokForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
        return render(request,"stok/stok_details.html",{
        "stok": form.instance
    })
    else:
        form = StokForm()
    return render(request,"stok/cihaz_ekle.html", {'form': form})



def cihaz_sil(request,slug):
    stok=Cihaz.objects.get(slug=slug)
    if request.method =="POST":
        stok.delete()
        return redirect("stoks")

    return render(request,"stok/cihaz_sil.html", {
        "stok": stok
    })
    

def cihaz_guncelle(request,slug):
    stok=Cihaz.objects.get(slug=slug)
    form= StokForm2( instance=stok)
    if request.method == 'POST':
        form = StokForm2(request.POST, instance=stok)
        if form.is_valid():
            form.save()
            return render(request,"stok/stok_details.html",{
        "stok": form.instance
    })                                              
    return render(request, 'stok/cihaz_guncelle.html', {'form': form})
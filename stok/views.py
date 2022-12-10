from unicodedata import category
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from stok.forms import StokForm
from stok.models import Employees, Devices, Departments, Categories, Status
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required



def index(request):         #ANA SAYFA
    context = {
        "stoks": Devices.objects.filter(
            Q(status__code="servise_alindi") | Q(status__code="servise-alindi")
        ),
        "categories": Categories.objects.all(),
    }
    return render(request, "stok/index.html", context)




def stoks(request):         #TÜM CİHAZLAR SAYFASI
    context = {
        "stoks": Devices.objects.all(),
        "categories": Categories.objects.all(),
    }
    return render(request, "stok/stoks.html", context)

def stok_details(request, slug):

    stok = Devices.objects.get(slug=slug)
    return render(request, "stok/stok_details.html", {"stok": stok})


def stoks_by_category(request, slug):
    context = {
        "stoks": Devices.objects.filter(category__slug=slug),
        "categories": Categories.objects.all(),
        "selected_category": slug,
    }
    return render(request, "stok/stoks.html", context)

@login_required(login_url='login')
def cihaz_ekle(request):
    form = StokForm(request.POST)
    if request.method == 'POST':
        form=StokForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "stok/stok_details.html",  {"stok": form.instance})
    else:
        form =StokForm()
    return render(request,"stok/cihaz_ekle.html", {'form': form})


    
    
    
    
    
    
    
    
    
    # if request.method == 'POST':
    #     form = StokForm(request.POST)
    #     if form.is_valid():
    #         form.save()

    # else:
    #     form = StokForm()
        
    # return render(request,"stok/cihaz_ekle.html", {'form': form})

@login_required(login_url='login')
def cihaz_sil(request, slug):
    stok = Devices.objects.get(slug=slug)
    if request.method == "POST":
        stok.delete()
        return redirect("stoks")

    return render(request, "stok/cihaz_sil.html", {"stok": stok})

@login_required(login_url='login')
def cihaz_guncelle(request, slug):
    stok = Devices.objects.get(slug=slug)
    form=StokForm(request.POST,instance=stok)
    if request.method == 'POST':
        form = StokForm(request.POST, instance=stok)
        if form.is_valid():
            form.save()
            return render(request, "stok/stok_details.html", {"stok": stok})
    else:
        stok = Devices.objects.get(slug=slug)
        form = StokForm(instance=stok)
    return render(request, "stok/cihaz_guncelle.html", {"form": form})

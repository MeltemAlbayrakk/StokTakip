from unicodedata import category
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from stok.forms import StokForm
from stok.models import Employees, Devices, Departments, Categories, Status
from datetime import datetime
from django.db.models import Q


# Create your views here.


def index(request):
    context = {
        "stoks": Devices.objects.filter(
            Q(status__code="servise_alindi") | Q(status__code="servise-alindi")
        ),
        "categories": Categories.objects.all(),
    }
    return render(request, "stok/index.html", context)


def stoks(request):
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


def cihaz_ekle(request):

    if request.method == "POST":
        print(50)
        form = StokForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "stok/stok_details.html", {"stok": form.instance})
    else:
        form = StokForm()
    return render(request, "stok/cihaz_ekle.html", {"form": form})


def cihaz_sil(request, slug):
    stok = Devices.objects.get(slug=slug)
    if request.method == "POST":
        stok.delete()
        return redirect("stoks")

    return render(request, "stok/cihaz_sil.html", {"stok": stok})


def cihaz_guncelle(request, slug):
    stok = Devices.objects.get(slug=slug)
    
    if request.method == "POST":
        print(500)
        form = StokForm(request.POST, instance=stok)
        if form.is_valid():
            
            form.save()
            return render(request, "stok/stok_details.html", {"stok": form.instance})
    form=StokForm(instance=stok)
    return render(request, "stok/cihaz_guncelle.html", {"form": form})

from unicodedata import category
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from stok.models import Bolum, Category, Cihaz
from datetime import datetime



# Create your views here.

def index(request):
    context ={
        "stoks":Cihaz.objects.filter(status=1),
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

    if request.method == "POST":
        marka_model = request.POST["marka_model"]
        image = request.POST["image"]
        description = request.POST["description"]
        SeriNo = request.POST["SeriNo"]
        personel = request.POST["personel"]
        status = request.POST["status"]
        giris_tarihi = request.POST["giris_tarihi"]
        cikis_tarihi = request.POST["cikis_tarihi"]
  


        
        cihaz = Cihaz.objects.create(marka_model=marka_model,image=image,description=description,SeriNo=SeriNo,
        personel=personel,status=status,giris_tarihi=giris_tarihi,cikis_tarihi=cikis_tarihi)
        cihaz.save()
        return redirect("stoks")
        
    return render(request,"stok/cihaz_ekle.html")


def cihaz_sil(request,slug):

    stok=Cihaz.objects.get(slug=slug)
    # if  request.method =="POST":
    #     stok.delete()
    return render(request,"stok/stoks.html")
    
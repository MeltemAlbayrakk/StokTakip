from django.urls import path

from . import views

from stok.views import *


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("stoks", views.stoks, name="stoks"),
    path("category/<slug:slug>", views.stoks_by_category, name="stoks_by_category"),
    path("stoks/<slug:slug>", views.stok_details, name="stok_details"),
    path("cihaz_ekle/", views.cihaz_ekle, name="cihaz_ekle"),
    path("cihaz_sil/<slug:slug>", views.cihaz_sil, name="cihaz_sil"),
    path("cihaz_guncelle/<slug:slug>", views.cihaz_guncelle, name="cihaz_guncelle"),
]

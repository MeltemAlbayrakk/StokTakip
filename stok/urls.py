from django.urls import path 
from .import views

#http://127.0.0.1:8000/            =>index
#http://127.0.0.1:8000/index       =>index
#http://127.0.0.1:8000/stoks       =>stoks
#http://127.0.0.1:8000/stoks/3     =>stoks-details



urlpatterns = [
    path("",views.index),
    path("index",views.index),
    path("stoks",views.stoks),
    path("stoks/<int:id>",views.stok_details),
    

]


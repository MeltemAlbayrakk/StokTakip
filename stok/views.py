from django.http.response import HttpResponse
from django.shortcuts import render

data={
    "stoks":[
        {
            "id":1,
            "title":"python kursu",
            "image": "python.jpeg",
            "is_active": True,
            "is_home": False,
            "description": "python kursu acıklama"
        },
        {
            "id":2,
            "title":"django krusu",
            "image": "django.png",
            "is_active": True,
            "is_home": True,
            "description": "django kursu acıklama"
        },
        {
            "id":3,
            "title":"js kursu",
            "image": "js.png",
            "is_active": False,
            "is_home": True,
            "description": "js kursu acıklama"
        }
    ]
}

# Create your views here.

def index(request):
    context ={
        "stoks":data["stoks"]
    }
    return render(request,"stok/index.html",context)

def stoks(request):
    context ={
        "stoks":data["stoks"]
    }
    return render(request,"stok/stoks.html",context)

def stok_details(request,id):
    return render(request,"stok/stok_details.html",{
        "id":id
    })

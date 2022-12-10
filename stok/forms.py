from django import forms
from .models import Devices
from django.contrib.auth.models import User


class StokForm(forms.ModelForm):
  
    class Meta:
        model = Devices
        fields = [
            "brand",
            "image",
            "description",
            "serialnum",
            "employee",
            "category",
            "status",
            "arrival_date",
            "exit_date",
            "department",
            "worker",
            ]
        
       
        
            
            
        

        

        
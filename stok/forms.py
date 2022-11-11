from django import forms
from .models import Cihaz


class StokForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Cihaz
        fields = ('marka_model', 'image','description','personel',"category",'SeriNo','status','giris_tarihi','cikis_tarihi','bolum')
        
class StokForm2(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Cihaz
        fields = ('marka_model', 'image','description','personel',"category",'SeriNo','status','giris_tarihi','cikis_tarihi','bolum')
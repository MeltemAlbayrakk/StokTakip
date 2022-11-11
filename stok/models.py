import datetime
from email.policy import default
from enum import unique
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField 
from datetime import date , datetime
from django.utils.translation import gettext_lazy as _




class Category(models.Model):
    name=models.CharField(max_length=150)
    slug= models.SlugField(null=False, blank=True, unique =True, db_index=True,editable=False)


    def save(self, *args,**kwargs):
        self.slug =slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):  
        return f"{self.name}"

class Bolum(models.Model):
    bolumAdi = models.CharField(max_length=150)

    def save(self, *args,**kwargs):
        self.slug =slugify(self.bolumAdi)
        super().save(*args,**kwargs)

    def __str__(self):  
        return f"{self.bolumAdi}"

class Cihaz(models.Model):
    class StatusChoices(models.TextChoices):
        SERVIS = "servise_alindi", _("Servise alındı")
        BEKLEMEDE = "bekleme", _("Beklemede")
        ONARIMDA = "onarimda", _("Onarılıyor")




    marka_model = models.CharField(max_length=200)
    image = models.ImageField(upload_to="stoks")
    description= RichTextField()
    SeriNo = models.CharField(max_length=200)
    personel = models.CharField(max_length=200)
    status = models.CharField(max_length=200,null=True,         choices=StatusChoices.choices,
)
    giris_tarihi = models.DateField(blank=True,null=True)
    cikis_tarihi = models.DateField(blank=True,null=True)
    slug= models.SlugField(null= False, unique=True ,blank=True, db_index=True, editable=False)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)
    bolum = models.ForeignKey(Bolum,on_delete=models.SET_NULL, null=True)
    # hicbir satÄ±rda bos deger kabul edilmedigi icin yenÄ± bÄ±r sÃ¼tun eklenirse sorun olusur

    def __str__(self):
            return f"{self.marka_model}"

    def save(self, *args,**kwargs):
        self.slug =slugify(self.marka_model)

        super().save(*args,**kwargs)

 




    



from email.policy import default
from random import choices
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField 
from datetime import datetime



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
    marka_model = models.CharField(max_length=200)
    image = models.ImageField(upload_to="stoks")
    description= RichTextField()
    SeriNo = models.CharField(max_length=200)
    personel = models.CharField(max_length=200)
    status = models.BooleanField(null=True)
    giris_tarihi = models.DateField(blank=True,null=True,default=datetime.date)
    cikis_tarihi = models.DateField(blank=True,null=True,default=datetime.date)
    slug= models.SlugField(null= False, blank=True, unique= True, db_index=True, editable=False)
    categories = models.ManyToManyField(Category, blank=True)
    bolums = models.ForeignKey(Bolum, on_delete=models.CASCADE)
    # hicbir satÄ±rda bos deger kabul edilmedigi icin yenÄ± bÄ±r sÃ¼tun eklenirse sorun olusur

    def __str__(self):
            return f"{self.marka_model}"

    def save(self, *args,**kwargs):
        self.slug =slugify(self.marka_model)

        super().save(*args,**kwargs)






    



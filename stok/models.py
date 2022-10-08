from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils.text import slugify

class Stok(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="stoks")
    description= models.TextField()
    is_active = models.BooleanField(default=False)
    is_home= models.BooleanField(default=False)
    slug= models.SlugField(null= False, blank=True, unique= True, db_index=True, editable=False)
    # hicbir satırda bos deger kabul edilmedigi icin yenı bır sütun eklenirse sorun olusur


    def __str__(self):
        return f"{self.title}"

    def save(self, *args,**kwargs):
        self.slug =slugify(self.title)

        super().save(*args,**kwargs)



class Category(models.Model):
    name=models.CharField(max_length=150)
    slug= models.SlugField(null=False, blank=True, unique =True, db_index=True,editable=False)


    def save(self, *args,**kwargs):
        self.slug =slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return f"{self.name}"
import datetime
from email.policy import default
from enum import unique
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from datetime import date, datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Departments(models.Model):
    dep_name = models.CharField(max_length=150,verbose_name="FAKÜLTE")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.dep_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.dep_name}"


class Employees(models.Model):
    emp_fname = models.CharField(max_length=50,verbose_name="AD")
    emp_lname = models.CharField(max_length=50,verbose_name="SOYAD")
    emp_tel = models.CharField(max_length=15,verbose_name="TELEFON")
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True,verbose_name="FAKÜLTE")
    emp_email = models.CharField(max_length=50,verbose_name="MAİL ADRESİ")

    def __str__(self):
        return f"{self.emp_fname}  {self.emp_lname}"


class Categories(models.Model):
    name = models.CharField(max_length=150,verbose_name="KATEGORİ")
    slug = models.SlugField(
        null=False, blank=True, unique=True, db_index=True, editable=False,verbose_name="SLUG"
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):

    name = models.CharField(max_length=200,verbose_name="DURUM")
    code = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


class Devices(models.Model):
    brand = models.CharField(max_length=50, verbose_name="MARKA-MODEL")
    image = models.ImageField(upload_to="stoks",verbose_name="FOTOĞRAF")
    serialnum = models.CharField(max_length=20,verbose_name="SERİ NUMARASI")
    description = RichTextField(verbose_name="AÇIKLAMA")
    arrival_date = models.DateField(null=True,verbose_name="GİRİŞ TARİHİ")
    exit_date = models.DateField(blank=True,null=True,verbose_name="ÇIKIŞ TARİHİ")
    employee = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True,verbose_name="PERSONEL")
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True,verbose_name="KATEGORİ")
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True,verbose_name="FAKÜLTE")
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,verbose_name="TEKNİKER")
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True,verbose_name="DURUM")
    slug = models.SlugField(
        null=False, unique=True, blank=True, db_index=True,verbose_name="SLUG"
    )

    def __str__(self):
        return f"{self.brand}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand)

        super().save(*args, **kwargs)

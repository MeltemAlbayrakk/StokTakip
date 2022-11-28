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
    dep_name = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.dep_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.dep_name}"


class Employees(models.Model):
    emp_fname = models.CharField(max_length=50)
    emp_lname = models.CharField(max_length=50)
    emp_tel = models.CharField(max_length=15)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    emp_email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.emp_fname}  {self.emp_lname}"


class Categories(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(
        null=False, blank=True, unique=True, db_index=True, editable=False
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"


class Devices(models.Model):
    brand = models.CharField(max_length=50, verbose_name="XX")
    image = models.ImageField(upload_to="stoks")
    serialnum = models.CharField(max_length=20)
    description = RichTextField(verbose_name="XX")
    arrival_date = models.DateField(blank=True,null=True)
    exit_date = models.DateField(blank=True,null=True)
    employee = models.ForeignKey(Employees, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, null=True)
    worker = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(
        null=False, unique=True, blank=True, db_index=True
    )

    def __str__(self):
        return f"{self.brand}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand)
        print(50)
        super().save(*args, **kwargs)

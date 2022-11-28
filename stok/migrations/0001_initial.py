# Generated by Django 3.2.9 on 2022-11-28 16:25

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categories",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("slug", models.SlugField(blank=True, editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Departments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dep_name", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        choices=[
                            ("servise_alindi", "Servise alındı"),
                            ("bekleme", "Beklemede"),
                            ("onarimda", "Onarılıyor"),
                            ("tamamlandi", "Tamamlandı"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Workers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("wor_fname", models.CharField(max_length=50)),
                ("wor_lname", models.CharField(max_length=50)),
                ("wor_telno", models.CharField(max_length=50)),
                ("username", models.CharField(max_length=50)),
                ("password", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("emp_fname", models.CharField(max_length=50)),
                ("emp_lname", models.CharField(max_length=50)),
                ("emp_tel", models.CharField(max_length=15)),
                ("emp_email", models.CharField(max_length=50)),
                (
                    "department",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="stok.departments",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Devices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("brand", models.CharField(max_length=50)),
                ("image", models.ImageField(upload_to="stoks")),
                ("serialnum", models.CharField(max_length=20)),
                ("description", ckeditor.fields.RichTextField()),
                ("arrival_date", models.DateField(blank=True)),
                ("exit_date", models.DateField(blank=True)),
                ("slug", models.SlugField(blank=True, editable=False, unique=True)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="stok.categories",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="stok.departments",
                    ),
                ),
                (
                    "employee",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="stok.employees",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="stok.status",
                    ),
                ),
                (
                    "worker",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="stok.workers",
                    ),
                ),
            ],
        ),
    ]

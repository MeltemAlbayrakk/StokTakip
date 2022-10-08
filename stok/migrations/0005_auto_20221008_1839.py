# Generated by Django 3.2.9 on 2022-10-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0004_auto_20221008_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='stok',
            name='image',
            field=models.ImageField(upload_to='stoks'),
        ),
    ]
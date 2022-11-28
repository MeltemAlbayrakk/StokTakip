# Generated by Django 3.2.9 on 2022-11-28 17:16

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0004_auto_20221128_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devices',
            name='arrival_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='devices',
            name='brand',
            field=models.CharField(max_length=50, verbose_name='XX'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='XX'),
        ),
        migrations.AlterField(
            model_name='devices',
            name='exit_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.9 on 2022-11-28 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stok", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="status",
            name="name",
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.9 on 2022-10-30 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0015_alter_cihaz_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cihaz',
            old_name='bolums',
            new_name='bolum',
        ),
    ]

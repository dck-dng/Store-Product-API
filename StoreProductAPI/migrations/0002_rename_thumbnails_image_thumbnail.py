# Generated by Django 4.2.4 on 2023-08-13 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StoreProductAPI', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='thumbnails',
            new_name='thumbnail',
        ),
    ]

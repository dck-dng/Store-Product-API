# Generated by Django 4.2.4 on 2023-08-13 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreProductAPI', '0002_rename_thumbnails_image_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
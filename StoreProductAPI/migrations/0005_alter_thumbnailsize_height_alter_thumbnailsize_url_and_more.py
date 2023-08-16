# Generated by Django 4.2.4 on 2023-08-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StoreProductAPI', '0004_alter_image_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnailsize',
            name='height',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='thumbnailsize',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='thumbnailsize',
            name='width',
            field=models.PositiveIntegerField(null=True),
        ),
    ]

# Generated by Django 2.2.13 on 2020-10-01 08:50

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0006_auto_20200930_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='picture',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]

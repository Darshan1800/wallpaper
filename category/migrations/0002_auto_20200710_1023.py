# Generated by Django 3.0.8 on 2020-07-10 04:53

import category.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='thumb',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=category.models.reference_main_image_path),
        ),
    ]
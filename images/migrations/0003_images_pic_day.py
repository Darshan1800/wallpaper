# Generated by Django 2.1.15 on 2020-08-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20200805_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='pic_day',
            field=models.BooleanField(default=True),
        ),
    ]

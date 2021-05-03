# Generated by Django 3.0.8 on 2020-07-10 04:53

from django.db import migrations, models
import django.db.models.deletion
import images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_auto_20200710_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('tags', models.TextField()),
                ('downloads', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('thumbnail', models.ImageField(blank=True, default='default.jpg', upload_to=images.models.reference_main_image_path)),
                ('hd', models.ImageField(blank=True, default='default.jpg', upload_to=images.models.reference_main_image_path)),
                ('fourk', models.ImageField(blank=True, default='default.jpg', upload_to=images.models.reference_main_image_path)),
                ('normal', models.ImageField(blank=True, default='default.jpg', upload_to=images.models.reference_main_image_path)),
                ('status', models.BooleanField(default=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='category.Category')),
            ],
        ),
    ]
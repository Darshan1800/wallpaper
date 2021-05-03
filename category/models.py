from django.db import models
from django.utils.safestring import mark_safe

def reference_main_image_path(instance, filename):
    sub_folder = instance.slug
    return f'categroy/{sub_folder}/{filename}'

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.jpg', blank=True, upload_to=reference_main_image_path)
    active=models.BooleanField(default=True)
    # add in author later
    
    def __str__(self):
        return self.title

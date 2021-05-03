from django.db import models

from django.urls import reverse

from category.models import Category

from django.utils.html import mark_safe
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from six import python_2_unicode_compatible
from taggit.managers import TaggableManager

def reference_main_image_path(instance, filename):
    sub_folder = instance.slug
    return f'images/{sub_folder}/{filename}'


@python_2_unicode_compatible
class Images(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()
    
    category = models.ForeignKey(Category,default=None,on_delete=models.CASCADE)

    thumbnail = models.ImageField(default='default.jpg', blank=True, upload_to=reference_main_image_path)
    hd = models.ImageField(default='default.jpg', blank=True, upload_to=reference_main_image_path)
    fourk = models.ImageField(default='default.jpg', blank=True, upload_to=reference_main_image_path)
    normal = models.ImageField(default='default.jpg', blank=True, upload_to=reference_main_image_path)
    desktop = models.ImageField(default='default.jpg', blank=True, upload_to=reference_main_image_path)
    
    
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    
    
    
    pic_day=models.BooleanField(default=False)

    status=models.BooleanField(default=True)
    # add in author later
    
    def __str__(self):
        return self.title

    
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Images, self).save(*args, **kwargs)
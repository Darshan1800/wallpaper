from django.contrib import admin
from django.utils.html import format_html
from .models import Images
class BookAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width=200 height=200/>'.format(obj.thumbnail.url))

    image_tag.short_description = 'Image'
    list_display = ('title', 'slug', 'date','image_tag')
    search_fields = ('title', 'slug' )
admin.site.register(Images, BookAdmin)
# admin.site.register(
#     Images
# )
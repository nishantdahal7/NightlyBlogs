
from django.contrib import admin
from .models import Category, Post

# Register your models here.

# for configuration of category admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'add_date']
    search_fields = ['title']
    list_per_page = 25


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'add_date']
    search_fields = ['title']
    list_filter = ['category']
    list_per_page = 50

    class Media:
        js = (
            'https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js', 'js/script.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

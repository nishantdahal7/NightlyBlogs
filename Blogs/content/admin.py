
from django.contrib import admin
from .models import Category, Post

# Register your models here.

# for configuration of category admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'add_date']
    list_display_links = ['title']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 25


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_tag', 'content', 'add_date', ]
    list_display_links = ['title']
    list_filter = ['title']
    search_fields = ['title']
    list_per_page = 25


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

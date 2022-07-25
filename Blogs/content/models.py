
from django.db import models
from django.utils.html import format_html


# Create your models here.

# Category model


class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

# Post Model


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='post/')
    url = models.CharField(max_length=100)
    add_date = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html('<img src="/media/{}" width="60" height="60" />'.format(self.image))

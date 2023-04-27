from django.contrib import admin
from .models import Post, Comment, Category, Image, Profile

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Profile)

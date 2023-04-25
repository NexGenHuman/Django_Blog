from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Image(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/')
    publication_date = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    body = RichTextField()
    header_image = models.ImageField(null=True, blank=True, upload_to='headers/')
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    requires_permission = models.BooleanField(default=False)
    password = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50)
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # Just remembered to add it :-P
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, upload_to='profile_images/')

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
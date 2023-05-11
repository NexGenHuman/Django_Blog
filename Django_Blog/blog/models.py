from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse

# Model naming convention:
# 1) Model names should be singular
# 2) Model names should be in PascalCase
# 3) Model names should be descriptive

# Field naming convention:
# 1) Field names should be in snake_case
# 2) Field names should be descriptive

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
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('post_detail', args=(str(self.id)))

    class Meta:
        ordering = ['-publication_date']    # default ordering for posts
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)
    publication_date = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)                
    tiktok = models.URLField(null=True, blank=True)                  
    twitter = models.URLField(null=True, blank=True)                 
    instagram = models.URLField(null=True, blank=True)               
    description = models.TextField(max_length=250)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profile_images/')

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
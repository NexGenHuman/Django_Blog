from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Model naming convention:
# 1) Model names should be singular
# 2) Model names should be in PascalCase
# 3) Model names should be descriptive

# Field naming convention:
# 1) Field names should be in snake_case
# 2) Field names should be descriptive

# --------------------- We should think about CharField lengths
class Image(models.Model):
    # --------------------- Should we add an author field?
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/')
    publication_date = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # --------------------- Should the post be deleted if the user is deleted?
    title = models.CharField(max_length=50)
    body = RichTextField()
    header_image = models.ImageField(null=True, blank=True, upload_to='headers/')
    publication_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    requires_permission = models.BooleanField(default=False)
    password = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50)
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) # --------------------- Should the comment be deleted if the user is deleted?
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # --------------------- Any more ideas for profile fields?
    description = models.TextField()
    profile_image = models.ImageField(null=True, blank=True, upload_to='profile_images/')

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='images/')
    publication_date = models.DateTimeField(auto_now_add=True)


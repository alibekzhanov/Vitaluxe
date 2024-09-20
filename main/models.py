from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=100)
    banner = models.FileField(upload_to='banners/')  # Supports images, videos, GIFs
    
    def __str__(self):
        return self.title

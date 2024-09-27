from django.db import models
from django.urls import reverse


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=100)
    banner = models.FileField(upload_to='banners/')  # Поддерживает изображения, видео, GIF-файлы
    
    def __str__(self):
        return self.title


class Product(models.Model):
    ratings = models.PositiveIntegerField(default=0)
    description = models.TextField()
    name = models.CharField(max_length=200)
    count = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')  # Изображение для карточки товара
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop_all')  # Перенаправляет на страницу shop_all
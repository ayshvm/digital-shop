from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploads/files', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='uploads/thumbnails')
    link = models.CharField(null=True, max_length=200, blank=True)
    fileSize = models.CharField(null=True, max_length=200)


class ProductImage(models.Model):
    # relationships between images and product as 1 product will have multiple image
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/images', blank=True)


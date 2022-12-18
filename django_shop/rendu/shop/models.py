from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    stock = models.PositiveIntegerField(default=10)
    price = models.FloatField(default=0)
    image = models.CharField(max_length=200)


from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'stock', 'price', 'image']

admin.site.register(Product)

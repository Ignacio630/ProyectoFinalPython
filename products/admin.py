from django.contrib import admin
from .models import Products
# Register your models here.



admin.site.register(Products)

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')
    search_fields = ('name', 'price', 'stock', 'category')
    list_filter = ('name', 'price', 'stock', 'category')
    list_per_page = 10

# Register your models here.


from django.db import models
from categories.models import Category
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.BooleanField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Nombre: {self.name} - Precio: {self.price} - Stock: {self.stock}"

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    def __str__(self):
        return self.title
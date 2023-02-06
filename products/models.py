from django.db import models
from categories.models import Category
# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.BooleanField()
    image = models.ImageField(upload_to='media/products', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Nombre: {self.name} - Precio: {self.price} - Stock: {self.stock}"

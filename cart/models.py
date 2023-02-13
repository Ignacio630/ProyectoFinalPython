from django.db import models
from products.models import Products
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    def __str__(self):
        return f"Nombre: {self.product.name} - Precio: {self.product.price} - Cantidad: {self.quantity} - Total: {self.total_price} - Usuario: {self.user}"
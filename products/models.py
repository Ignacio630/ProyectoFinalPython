from django.db import models
from categories.models import Category


class Products(models.Model):
    # categories = Category.objects.all()
    
    # for category in categories:
    #     categoryID = category.id
    #     categoryName = category.name
        
        
    # CONDITION_CHOICES = (
    #     (categoryID, categoryName),
    # )
        
    name = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(null=True, blank=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    # category = models.CharField(max_length=50, choices=CONDITION_CHOICES)

    def __str__(self) -> str:
        return f"ID:{self.id} Nombre: {self.name} - {self.descripcion} - Precio: {self.price} - Stock: {self.stock}"

from django import forms 
from categories.models import Category

class ProductsForm(forms.Form):
    name = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=300)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = forms.BooleanField()
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    
    def __str__(self) -> str:
        return f"Nombre: {self.name} - Precio: {self.price} - Stock: {self.stock}"

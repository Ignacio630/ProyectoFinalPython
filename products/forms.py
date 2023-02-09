from django import forms 
from django.db import models
from .models import Products
from categories.models import Category

class ProductsForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(max_length=300, required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = forms.BooleanField()
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model = Products
        fields = ['name', 'descripcion', 'price', 'stock', 'image', 'category']        
        


class UpdateProductsForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    descripcion = forms.CharField(max_length=300, required=True)
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    stock = forms.BooleanField()
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model = Products
        fields = ['name', 'descripcion', 'price', 'stock', 'image', 'category']
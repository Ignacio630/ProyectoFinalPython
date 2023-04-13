from django import forms 
from django.db import models
from .models import Products
from categories.models import Category

class ProductsForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True, label='Nombre del producto', widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(max_length=300, required=True, label='Descripción del producto', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'cols': 3}))
    price = forms.DecimalField(max_digits=10, decimal_places=2, required=True, label='Precio del producto', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    stock = forms.BooleanField(required=False, label='¿En stock?', widget=forms.CheckboxInput(attrs={'class': 'form-check-inline' }))
    image = forms.ImageField(required=True, label='Imagen del producto')
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True, label='Categoría del producto', widget=forms.Select(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Products
        fields = ['name', 'descripcion', 'price', 'stock', 'image', 'category']
            
        


class UpdateProductsForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=300)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = forms.BooleanField(required=False)
    image = forms.ImageField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model = Products
        fields = ['name', 'descripcion', 'price', 'stock', 'image', 'category']
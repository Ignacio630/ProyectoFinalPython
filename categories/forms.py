from django import forms 
from .models import Category



class CategoryForm(forms.ModelForm):

    name = forms.CharField(label='Nombre de la categoria', max_length=100)

    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
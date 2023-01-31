from django import forms 

class Products(forms.form):
    name = forms.CharField(max_length=100)
    descripcion = forms.CharField(max_length=300)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    stock = forms.BooleanField()
    image = forms.ImageField()

    def __str__(self) -> str:
        return f"Nombre: {self.name} - Precio: {self.price} - Stock: {self.stock}"
from django.shortcuts import render
<<<<<<< HEAD
from .models import Products
from .forms import Products
# Create your views here.


def create_product(request):
    product = Products.objects.create()

    context = {

    }
    return render(request, '', context=context)
=======

# Create your views here.

def create_product(request):
    return render(request, 'products/create_product.html', {})
>>>>>>> f066075d74f239665bb3f466439d1764f41310dd

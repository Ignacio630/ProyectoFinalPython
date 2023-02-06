from django.shortcuts import render, redirect
from django.db import IntegrityError
from .models import Products
from .forms import ProductsForm
from categories.models import Category
# Create your views here.

def create_product(request):

    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'form': ProductsForm,
            'error': 'Please fill all the fields',
            'categories': categories,
        }
        return render(request, 'products/create_product.html', context=context)
    else:
        if request.POST['name'] and request.POST['descripcion'] and request.POST['price'] and request.POST['stock'] and request.POST['image'] and request.POST['category' == '']:
            try:
                product = Products.objects.create(name=request.POST['name'], descripcion=request.POST['descripcion'], price=request.POST['price'], stock=request.POST['stock'], image=request.POST['image'], category=request.POST['category'])
                product.save()
                return redirect('home_page')
            except IntegrityError:
                context = {
                    'form': ProductsForm,
                    'categories': categories,
                    'error': 'Product has already been taken. Please choose a new product.'
                }
                return render(request, 'products/create_product.html', context=context)

def detail_product(request, product_id):
    product = Products.objects.get(pk=product_id)
        
    if request.method == 'GET':
        context = {
            'product': product,
        }
        return render(request, 'products/detail_product.html', context=context)
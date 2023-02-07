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
            'categories': categories,
        }
        return render(request, 'products/create_product.html', context=context)
    else:
        if request.POST['name'] or request.POST['descripcion'] or request.POST['price'] or request.POST['stock'] or request.POST['image'] or request.POST['category']:
            try:
                product = Products.objects.create(name=request.POST['name'], descripcion=request.POST['descripcion'], price=request.POST['price'], stock=request.POST['stock'], image=request.POST['image'], category=request.POST['category'])
                print(product)
                product.save()
                return redirect('home_page')
            except IntegrityError:
                context = {
                    'form': ProductsForm,
                    'categories': categories,
                    'error': 'Product has already been taken. Please choose a new product.'
                }
                return render(request, 'products/create_product.html', context=context)
        else:
            context = {
                'form': ProductsForm,
                'categories': categories,
                'error': 'All fields are required.'
            }
            return render(request, 'products/create_product.html', context=context)

def detail_product(request, product_id):
    product = Products.objects.get(pk=product_id)
        
    if request.method == 'GET':
        context = {
            'product': product,
        }
        return render(request, 'products/detail_product.html', context=context)


def delete_product(request, product_id):
    
    if request.method == 'GET':
        product = Products.objects.get(pk=product_id)
        product.delete()
        return redirect('home_page')

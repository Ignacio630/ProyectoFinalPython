from django.shortcuts import render, redirect
from .models import Products  
from .forms import ProductsForm
from categories.models import Category
from django.contrib.auth.decorators import login_required

# Create your views here.


def create_product(request):
    if request.method == 'POST':
        formProduct = ProductsForm(request.POST, request.FILES)
        print(formProduct)
        if formProduct.is_valid():
            info = formProduct.cleaned_data
            name = info['name']
            descripcion = info['descripcion']
            price = info['price']
            stock = info['stock']
            image = info['image']
            category = info['category']
            product = Products(name=name, descripcion=descripcion, price=price, stock=stock, image=image, category=category)
            product.save()
            return redirect('home_page')
        else:
            categories = Category.objects.all()
            context = {
                'form': formProduct,
                'categories': categories,
                'error': 'Error al crear el producto',
            }
            return render(request, 'products/create_product.html', context=context)
    else:
        categories = Category.objects.all()
        context = {
            'form': ProductsForm,
            'categories': categories,
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

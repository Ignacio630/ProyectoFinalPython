from django.shortcuts import render, redirect 
from .models import Products  
from .forms import ProductsForm, UpdateProductsForm
from categories.models import Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.


def create_product(request):
    if request.method == 'POST':
        formProduct = ProductsForm(request.POST, request.FILES)
        if formProduct.is_valid():
            product = formProduct.save(commit=False)
            product.save()
            return redirect('home_page')
        else:
            context = {
                'form': formProduct,
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
    product = get_object_or_404(Products, pk=product_id)
        
    if request.method == 'GET':
        context = {
            'product': product,
        }
        return render(request, 'products/detail_product.html', context=context)
    else:
        context = {
            'error': 'Error al mostrar el producto',
        }
        return render(request, 'products/detail_product.html', context=context)
    
@login_required
def update_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)    
    
    if request.method == 'GET':
        form = UpdateProductsForm(instance=product)
        context = {
            'form': form,
            'product': product,
            'categories': Category.objects.all(),
        }
        return render(request, 'products/update_product.html', context=context)
    elif request.method == 'POST':
        form = UpdateProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            info = form.cleaned_data
            
            product.name = info['name']
            product.descripcion = info['descripcion']
            product.price = info['price']
            product.stock = info['stock']
            product.image = info['image']
            product.category = info['category']

            form.save()
            return redirect('detail_product', product_id=product.id)
        else:
            context = {
                'form': form,
                'product': product,
                'categories': Category.objects.all(),
                'error': 'Error al actualizar el producto',
                'form_errors': form.errors,
            }
            return render(request, 'products/update_product.html', context=context)

def delete_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
<<<<<<< HEAD
    print(product)
    if request.method == 'POST':
        product.delete()
        return redirect('home_page')
    else:
=======
    
    if request.method == 'GET':
>>>>>>> 4fee19c3ba9e6765a25822ec7c5197a82833d401
        context = {
            'product': product,
        }
        return render(request, 'products/delete_product.html', context=context)
    elif request.method == 'POST':
        product.delete()
        return redirect('home_page')

def list_products(request):
    if request.method == 'GET':
        products = Products.objects.all()
        categories = Category.objects.all()
        num_products = Products.objects.count()
        
        if  num_products > 0:
            context = {
                'products': products,
                'categories': categories,
            }
            return render(request, 'products/list_products.html', context=context)
        else:
            context = {
                'products': products,
                'categories': categories,
                'error': 'No hay productos',
            }
            return render(request, 'products/list_products.html', context=context)
    else:
        context = {
            'error': 'Error al listar los productos',
        }
        return render(request, 'products/list_products.html', context=context)

def list_products_by_category(request, category_id):
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    products = Products.objects.filter(category=category)
    context = {
        'categories': categories,
        'category': category,
        'products': products,
    }
    return render(request, 'products/list_products_by_category.html', context=context)

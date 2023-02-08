from django.shortcuts import render, redirect
from .models import Products  
from .forms import ProductsForm
from categories.models import Category
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_product(request):
    if request.method == 'GET':
        
        form = ProductsForm()
        context = {
            'form': form,
        }
        return render(request, 'products/create_product.html', context=context)
        
    else:
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = Products.objects.create(
            product.save()   
            return redirect('home_page')
        else:
            context = {
                'form': form,
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

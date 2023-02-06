from django.shortcuts import render
from .models import Products
from .forms import Products
# Create your views here.

def create_product(request):
    product = Products.objects.create()

    context = {
        'product': product
    }
    return render(request, 'products/', context=context)

def detail_product(request):
    product = Products.objects.get(id=request.product.id)

    if request.method == 'GET':
        context = {
            'product': product
        }
        return render(request, 'products/detail_product.html', context=context)
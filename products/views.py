from django.shortcuts import render

# Create your views here.

def create_product(request):
    return render(request, 'products/create_product.html', {})
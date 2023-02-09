from django.shortcuts import render
from categories.models import Category
from products.models import Products

def home_page(request):

    categories = Category.objects.all()
    listProducts = Products.objects.all()
    print(listProducts)
    context = {
        'categories': categories,
        'products': listProducts,
    }
    return render(request, "layouts/home_page.html", context=context)

def base(request):

    categories = Category.objects.all()
    listProducts = Products.objects.all()
    print(listProducts)
    context = {
        'categories': categories,
        'products': listProducts,
    }
    return render(request, "base.html", context=context)

from django.shortcuts import render
from categories.models import Category
from products.models import Products

def home_page(request):

    categories = Category.objects.all()
    products = Products.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, "layouts/home_page.html", context=context)



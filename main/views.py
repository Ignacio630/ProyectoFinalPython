from django.shortcuts import render
from categories.models import Category
from products.models import Products

def home_page(request):

    categories = Category.objects.all()
    listProducts = Products.objects.all()
    
    context = {
        'categories': categories,
        'products': listProducts,
        'url': listProducts[0].image.url,
    }
    return render(request, "layouts/home_page.html", context=context)
    

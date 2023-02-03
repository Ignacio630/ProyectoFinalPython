from django.shortcuts import render
from categories.models import Category
from products.models import Product

def home_page(request):

    categories = Category.objects.all()
    # products = Product.objects.all()
    context = {
        'categories': categories,
        # 'products': products,
    }
    return render(request, "layouts/home_page.html", context=context)



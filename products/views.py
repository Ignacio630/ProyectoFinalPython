from django.shortcuts import render
from .models import Products
from .forms import Products
# Create your views here.


def create_product(request):
    product = Products.objects.create()

    context = {

    }
    return render(request, '', context=context)
from django.shortcuts import render
from django.contrib.auth.models import User
from categories.models import Category

def home_page(request):
    categories = Category.objects.all()
    context = {
        "categories": categories,
    }

    return render(request, "layouts/home_page.html", context=context)

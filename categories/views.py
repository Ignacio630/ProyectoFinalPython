from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm
# Create your views here.

def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = CategoryForm()
    return render(request, 'categories/create_category.html', {'form': form})

def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('home_page')
        
def update_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'categories/update_category.html', {'form': form})
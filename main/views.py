from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from categories.models import Category
from products.models import Product

def home_page(request):

    categories = Category.objects.all()
    # products = Product.objects.all()
    context = {
        'categories': categories,
        #'products': products,
    }

    return render(request, "layouts/home_page.html", context=context)


def register_form(request):
    if request.method == 'GET':
        return render(request, 'users/register.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home_page')
            except IntegrityError:
                return render(request, 'users/register.html', {'form': UserCreationForm, 'error': 'Username has already been taken. Please choose a new username.'})
        return render(request, 'users/register.html', {'form': UserCreationForm, 'error': 'Passwords did not match.'})

def user_profile(request):
    if request.method == 'GET':
        return render(request, 'users/user_profile.html')
    
def user_profile_edit(request, id):

    user = User.objects.get(id=request.user.id)
    if request.method == 'GET':
        
def login_form(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm,
        }
        return render(request, 'users/login.html', context=context)
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        
        if user is None:
            context = {
            'form': AuthenticationForm,
            'error': 'Nombre de usuario o contraseña incorrecta'
            }
            return render(request, 'users/login.html', context=context)
        else:
            login(request, user)
            return redirect('home_page')
            

def logout_user(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home_page')

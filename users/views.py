from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
# Create your views here.


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
            

def signout(request):
    if request.method == 'GET':
        logout(request)
        return redirect('home_page')

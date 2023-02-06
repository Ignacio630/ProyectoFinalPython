from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import UserEditForm


def login_form(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm,
        }
        return render(request, 'users/login.html', context=context)
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
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

# CRUD
# Create user


def register_form(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm,
        }
        return render(request, 'users/register.html', context=context)
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'],email=request.POST['email'], first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                user.save()
                login(request, user)
                return redirect('home_page')
            except IntegrityError:
                context = {
                    'form': UserCreationForm,
                    'error': 'Username has already been taken. Please choose a new username.'
                }
                return render(request, 'users/register.html', context=context)

    context = {
        'form': UserCreationForm,
        'error': 'Las contraseñas no coinciden'
    }
    return render(request, 'users/register.html', context=context)

# Read user


@login_required
def user_profile(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'GET':
        context = {
            'user': user,
        }
        return render(request, 'users/profile.html', context=context)

# Update user


@login_required
def update_user(request):
    user = request.user
    if request.method == 'POST':
        formEdit = UserEditForm(request.POST)
        if formEdit.is_valid():
            info = formEdit.cleaned_data
            if info['password1'] == info['password2']:
                user.username = info['username']
                user.email = info['email']
                user.first_name = info['first_name']
                user.last_name = info['last_name']
                user.set_password(info['password1'])
                user.save()
                return redirect('user_profile')
            else:
                context = {
                    'user': user,
                    'form': formEdit,
                    'error': 'Las contraseñas no coinciden'
                }
                return render(request, 'users/update.html', context=context)
        else:
            context = {
                'user': user,
                'form': formEdit,
            }
            return render(request, 'users/update.html', context=context)
    else:
        context = {
            'user': user,
            'form': UserEditForm,
        }
        return render(request, 'users/update.html', context=context)

# Delete user


def delete_user_btn(request):
    if request.method == 'GET':
        return render(request, 'users/delete.html')


@login_required
def delete_user(request):
    user = User.objects.get(id=request.user.id)
    user.delete()
    return redirect('home_page')

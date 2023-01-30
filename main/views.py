from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

def home_page(request):
    
    return render(request, "layouts/home_page.html")

from django.urls import path
from views import create_product

urlpatterns = [
    path('products/', create_product),

]
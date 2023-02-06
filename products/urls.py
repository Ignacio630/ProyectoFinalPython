from django.urls import path
from .views import create_product, detail_product

urlpatterns = [
    path('products/', create_product, name='create_product'),
    path('products/detail/', detail_product, name='detail_product'),

]
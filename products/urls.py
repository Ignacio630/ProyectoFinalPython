from django.urls import path
from .views import create_product, detail_product

urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('<int:product_id>/', detail_product, name='detail_product'),

]
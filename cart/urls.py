from django.urls import path
from .views import cart_product, add_product, delete_product_cart

urlpatterns = [
    path('cart/', cart_product, name='cart_products'),
    path('add/<int:product_id>/', add_product, name='add_product'),
    path('delete/<int:product_id>/', delete_product_cart, name='delete_product_cart'),
]

from django.urls import path
from .views import create_product, detail_product, delete_product, update_product,list_products ,list_products_by_category

urlpatterns = [
    path('create_product/', create_product, name='create_product'),
    path('<int:product_id>/', detail_product, name='detail_product'),
    path('update/<int:product_id>/', update_product, name='update_product'),
    path('delete/<int:product_id>/', delete_product, name='delete_product'),
    path('List_products/', list_products, name='list_products'),
    path('categories/<int:category_id>/', list_products_by_category, name='list_products_by_category'),
]
from django.urls import path
from .views import create_category, delete_category, update_category


urlpatterns = [
    path('create_category/', create_category, name='create_category'),
    path('delete_category/', delete_category, name='delete_category'),
    path('update_category/', update_category, name='update_category'),
]
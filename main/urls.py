from django.contrib import admin
from django.urls import path
from .views import home_page, register_form, login_form, logout_user, user_profile, update_user ,delete_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('users/logout_user/', logout_user, name='logout_user'),
    path('users/register/', register_form, name='register_form'),
    path('users/login/', login_form, name='login_form'),
    path('users/profile/', user_profile, name='user_profile'),
    path('users/edit/', update_user, name='update_user'),
    path('users/delete/',delete_user, name='delete_user'),
]

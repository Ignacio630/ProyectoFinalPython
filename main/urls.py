from django.contrib import admin
from django.urls import path
from .views import home_page, register_form, login_form, logout_user, user_profile, user_profile_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('users/logout_user/', logout_user, name='logout_user'),
    path('users/register/', register_form, name='register_form'),
    path('users/login/', login_form, name='login_form'),
    path('users/profile/<id>', user_profile, name='user_profile'),
    path('users/edit/', user_profile_edit, name='user_profile_edit'),
]

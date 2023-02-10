from django.urls import path
from .views import register_form, login_form, logout_user, user_profile, update_user, delete_user, update_password

urlpatterns = [
    path('users/logout_user/', logout_user, name='logout_user'),
    path('users/register/', register_form, name='register_form'),
    path('users/login/', login_form, name='login_form'),
    path('users/profile/', user_profile, name='user_profile'),
    path('users/edit/', update_user, name='update_user'),
    path('users/edit_password/', update_password, name='update_password'),
    path('users/delete/',delete_user, name='delete_user'),
    
]

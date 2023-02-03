from django.urls import path
from .views import register_form, login_form, logout_user, user_profile, update_user, delete_user, delete_user_btn

urlpatterns = [
    path('users/logout_user/', logout_user, name='logout_user'),
    path('users/register/', register_form, name='register_form'),
    path('users/login/', login_form, name='login_form'),
    path('users/profile/', user_profile, name='user_profile'),
    path('users/edit/', update_user, name='update_user'),
    path('users/delete_btn/', delete_user_btn, name='delete_user_btn'),
    path('users/delete/',delete_user, name='delete_user'),
]

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from .views import home_page
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('users/', include('users.urls')),
]

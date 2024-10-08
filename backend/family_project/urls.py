from django.contrib import admin
from django.urls import path
from family.views import create_family, home  # Add 'home' here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_family/', create_family, name='create_family'),
    path('', home, name='home'),  # Add this line for the root URL
]
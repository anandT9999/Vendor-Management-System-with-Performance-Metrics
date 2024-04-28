# urls.py in the main project directory

from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('vendor_management.urls')),  # Replace 'myapp' with your app's name
]

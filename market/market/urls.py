
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('profiles/', include('profiles.urls')),
    path('products/', include('products.urls')),
    path('admin/', admin.site.urls),      
]

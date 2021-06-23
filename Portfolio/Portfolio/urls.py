
from django.urls import path, include 
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('port/', include('port.urls')),
    path('admin/', admin.site.urls),
]

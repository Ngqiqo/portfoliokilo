from django.urls import path, include

from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    path('port/', include('port.urls')),
    path('admin/', admin.site.urls),
]

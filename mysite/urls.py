from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('autotag/', include('autotag.urls')),
    path('admin/', admin.site.urls),
]
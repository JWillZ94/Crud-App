from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('crud/', include('crud.urls')),
    path('admin/', admin.site.urls),
]

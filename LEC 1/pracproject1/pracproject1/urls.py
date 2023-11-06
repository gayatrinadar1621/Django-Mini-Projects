from django.contrib import admin
from django.urls import path
from pracapp1.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home)
]

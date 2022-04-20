from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',include('neighbourhood_app.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('tinymce/', include('tinymce.urls')),
]

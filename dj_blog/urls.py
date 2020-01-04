
from django.contrib import admin
from django.urls import path, include
from blog import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

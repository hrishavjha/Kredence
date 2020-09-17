from django.contrib import admin
from django.urls import path

from initial.views import hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/hello/', hello, name='hello'),
]

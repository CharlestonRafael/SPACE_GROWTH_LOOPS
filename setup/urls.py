from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_growth_loop.urls')),
    path('', include('usuarios.urls'))
]

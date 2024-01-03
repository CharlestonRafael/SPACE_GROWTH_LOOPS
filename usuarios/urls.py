from django.urls import path
from my_growth_loop.views import index

urlpatterns = [
    path('', index, name='index'),
]
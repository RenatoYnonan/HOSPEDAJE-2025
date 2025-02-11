from django.urls import path

from .views import *

urlpatterns = [
    path('', ClientesView.as_view(), name='index-clientes'),
]
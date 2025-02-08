from django.urls import path

from .views import *

urlpatterns = [
    path('', ClientesView.as_view(), name='index-clientes'),
    path('nuevo-cliente', CreateClientesView.as_view(), name='crear-cliente'),
]
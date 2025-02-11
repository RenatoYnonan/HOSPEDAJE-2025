from django.urls import path

from .views import *

urlpatterns = [
    path('', ClientesView.as_view(), name='index-clientes'),
    path('nuevo-cliente', CreateClientes.as_view(), name='crear-cliente'),
    path('edit-cliente/<int:pk>', UpdateClientes.as_view(), name='editar-cliente'),
]
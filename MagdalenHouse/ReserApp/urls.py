from django.urls import path
from .views import *

urlpatterns = [
    #Calendario
    path('calendario/', CalendarioView.as_view(), name='index-calendar'),
    path('reservas/', ObtenerReservas, name='index-reservas'),

    #Reservas
    path('nueva-reserva', ReservasView.as_view(), name='new-reserva'),
    path('edit-reserva/<int:pk>/', ReservaUpdate.as_view(), name='edit-reserva')
]

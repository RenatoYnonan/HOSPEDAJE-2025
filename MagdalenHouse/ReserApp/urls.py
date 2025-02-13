from django.urls import path
from .views import *

urlpatterns = [
    path('nueva-reserva', ReservasView.as_view(), name='new-reserva'),
    path('edit-reserva/<int:pk>/', ReservaUpdate.as_view(), name='edit-reserva')
    
]


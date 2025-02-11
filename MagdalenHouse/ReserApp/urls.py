from django.urls import path
from .views import *

urlpatterns = [
    path('nueva-reserva', ReservasView.as_view(), name='new-reserva'),
    
]


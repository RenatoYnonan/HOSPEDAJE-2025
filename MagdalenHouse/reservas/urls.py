from django.urls import path
from .views import CalendarioView, ReservasView


urlpatterns = [
    path('', CalendarioView.as_view(), name='index-calendar'),
    path('nueva-reserva', ReservasView.as_view(), name='new-reserva'),
    
]
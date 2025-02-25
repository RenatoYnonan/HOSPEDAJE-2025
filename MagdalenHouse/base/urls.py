from django.urls import path
from . import views


urlpatterns = [
    path('', views.HospedajeView.as_view(), name='hospedaje-magdalen'),
    path('detail-habitacion/<int:pk>/', views.DetailAlojamiento.as_view(), name='detail-habitacion'),
    path('resultados/', views.habitaciones_disponibles, name='resultados'),
    path('gracias/', views.Gracias.as_view(), name='gracias'),
    path('reservar-add/', views.crear_reserva, name='reservas-add-mh'),
]
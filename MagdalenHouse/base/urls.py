from django.urls import path
from . import views


urlpatterns = [
    path('', views.HospedajeView.as_view(), name='hospedaje-magdalen'),
    path('detail-habitacion/<int:pk>/', views.DetailAlojamiento.as_view(), name='detail-habitacion'),
]
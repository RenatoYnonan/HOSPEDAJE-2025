from django.urls import path
from .views import *

urlpatterns = [
    path('habitaciones/', Habitaciones.as_view(), name='index-habitacion'),
    path('habitaciones/create/', CreateHabitaciones.as_view(), name='create-habitacion'),
    path('habitaciones/update/<int:pk>', UpdateHabitaciones.as_view(), name='update-habitacion'),

    path('departamentos/', DepartamentosView.as_view(), name='index-departamento'),
    path('departamentos/create/', CreateDepartamentos.as_view(), name='create-departamento'),
    path('departamentos/update/<int:pk>', UpdateDepartamentos.as_view(), name='update-departamento'),
    path('delete-departamentos/<int:id>/', DeleteDepartament, name='delete-departamento'),
]
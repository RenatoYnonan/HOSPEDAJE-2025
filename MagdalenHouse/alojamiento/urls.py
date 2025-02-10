from django.urls import path
from .views import *

urlpatterns = [
    path('habitaciones/', Habitaciones.as_view(), name='index-habitacion'),
    path('habitaciones/create/', CreateHabitaciones.as_view(), name='create-habitacion'),
    path('habitaciones/update/<int:id>', UpdateHabitaciones.as_view(), name='update-habitacion'),
    path('habitaciones/delete/<int:id>', DeleteHabitaciones, name='delete-habitacion'),

    path('departamentos/', Departamentos.as_view(), name='index-departamento'),
    path('departamentos/create/', CreateDepartamentos.as_view(), name='create-departamento'),
    path('departamentos/update/<int:id>', UpdateDepartamentos.as_view(), name='update-departamento'),
    path('departamentos/delete/<int:id>', DeleteDepartamentos, name='delete-departamento'),
]
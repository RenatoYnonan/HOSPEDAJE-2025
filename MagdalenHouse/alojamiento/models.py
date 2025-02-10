from django.db import models

# Create your models here.
class Alojamiento(models.Model):
    name_booking =  models.CharField(max_length=255, unique=True ,verbose_name='Nombre del Alojamiento')
    description_booking = models.TextField(max_length=255, verbose_name='Descripción del Alojamiento')
    price_night = models.DecimalField(max_digits=10, decimal_places=2 ,verbose_name='Precio por noche')
    capacity_booking = models.IntegerField(verbose_name='Capacidad Maxima')
    size_booking = models.CharField(max_length=50, verbose_name='Tamaño del Alojamiento')
    active_booking = models.BooleanField(default=True, verbose_name='Estado del Alojamiento')

    class Meta:
        abstract  = True
    
    def __str__(self):
        return self.name_booking


class Habitaciones(Alojamiento):
    TIPO_HABITACION = [
        ('Doble', 'Doble'),
        ('Matrimonial', 'Matrimonial'),
        ('Triple', 'Triple'),
        ('Familiar', 'Familiar')
    ]

    type_booking =  models.CharField(max_length=150, choices=TIPO_HABITACION, verbose_name='Tipo de habitación')

    class Meta:
        verbose_name = 'Habitación'
        verbose_name_plural = 'Habitaciones'
        db_table = 'Habitaciones'

class Departamentos(Alojamiento):
    
    costo_limpieza = models.DecimalField(
        max_digits=10, decimal_places=2, default=50.00, 
        help_text="Costo fijo por servicio de limpieza (S/50.00)"
    )

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural  = 'Departamentos'
        db_table = 'Departamentos'
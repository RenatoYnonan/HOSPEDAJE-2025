from django.db import models
from clientes.models import ModelsClientes
from alojamiento.models import Alojamiento, Departamentos, Habitaciones

# Create your models here.
class Reserva(models.Model):
    ESTADOS_RESERVA = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    customer_selection = models.ForeignKey(ModelsClientes, on_delete=models.CASCADE, related_name='Cliente', blank=True, null=True)
    rooms = models.ManyToManyField(Habitaciones, blank=True)
    department = models.ManyToManyField(Departamentos, blank=True)
    date_start = models.DateField()
    date_end = models.DateField()
    active_booking = models.CharField(max_length=15, choices=ESTADOS_RESERVA, default='pendiente')

            

    def __str__(self):  
        alojamiento = self.rooms if self.rooms.exists() else self.department
        return f"Reserva {self.id} - {self.customer_selection.name_customer} {self.customer_selection.last_name_customer}"
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        db_table = 'reservas'
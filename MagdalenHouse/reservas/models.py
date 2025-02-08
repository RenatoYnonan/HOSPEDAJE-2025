from django.db import models
from clientes.models import ModelsClientes

# Create your models here.
class Reserva(ModelsClientes):
    ESTADOS_RESERVA = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]

    date_start = models.DateField()
    date_end = models.DateField()
    active_booking = models.CharField(max_length=15, choices=ESTADOS_RESERVA, default='pendiente')

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente.name_customer} {self.cliente.last_name_customer}"
    
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'
        db_table = 'reservas'
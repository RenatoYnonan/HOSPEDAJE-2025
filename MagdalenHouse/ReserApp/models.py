from django.db import models
from clientes.models import ModelsClientes

# Create your models here.
class ModelsReservas(models.Model):
    ESTADOS_RESERVA = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
    ]
    id = models.AutoField(primary_key=True)
    customer_selection = models.ForeignKey(ModelsClientes, on_delete=models.CASCADE, related_name='Cliente', blank=True, null=True)
    date_start = models.DateField(verbose_name='Fecha de inicio')
    date_end = models.DateField(verbose_name='Fecha de fin')
    active_booking = models.CharField(max_length=15, choices=ESTADOS_RESERVA, default='pendiente')
            
    
    class Meta:
        verbose_name = 'ModelsReservas'
        verbose_name_plural = 'ModelsReservas'
        db_table = 'ModelsReservas'
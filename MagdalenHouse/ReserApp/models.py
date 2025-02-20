from django.core import validators
from django.db import models
from clientes.models import ModelsClientes
from django.utils import timezone
from alojamiento.models import *
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class ModelsReservas(models.Model):
    ESTADOS_RESERVA = [
        ('pendiente', 'Pendiente'), # Adelanto del 50% del precio de la reserva
        ('confirmada', 'Confirmada'), # Adelanto del 100% del precio de la reserva
        ('completada', 'Completada'), # Estancia con check-in y check-out realizados
    ]
    id = models.AutoField(primary_key=True)
    customer_selection = models.ForeignKey(ModelsClientes, on_delete=models.CASCADE, related_name='Cliente', blank=True, null=True)
    departamento_selection = models.ForeignKey(Departamentos, on_delete=models.CASCADE, related_name='Departamento', blank=True, null=True)
    date_start = models.DateField(verbose_name='Fecha de inicio')
    date_end = models.DateField(verbose_name='Fecha de fin')
    number_nights = models.IntegerField(verbose_name='N°. Noches')
    number_people = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)],verbose_name='Cantidad de personas')
    date_create_customer = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    active_booking = models.CharField(max_length=15, choices=ESTADOS_RESERVA, default='pendiente')
    amount_paid = models.DecimalField(validators=[MinValueValidator(0)] ,max_digits=10, decimal_places=2, verbose_name='Monto Pagado', default=0)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Total')

    def save(self, *args, **kwargs):

        if self.active_booking is None:
            self.active_booking = 'pendiente'
            
        if self.date_start and self.date_end:
            self.number_nights = max((self.date_end - self.date_start).days, 0)
        super().save(*args, **kwargs)
      
    
    class Meta:
        verbose_name = 'ModelsReservas'
        verbose_name_plural = 'ModelsReservas'
        db_table = 'ModelsReservas'
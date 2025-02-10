# Generated by Django 4.2.16 on 2025-02-10 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('modelsclientes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clientes.modelsclientes')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('active_booking', models.CharField(choices=[('pendiente', 'Pendiente'), ('confirmada', 'Confirmada'), ('cancelada', 'Cancelada'), ('completada', 'Completada')], default='pendiente', max_length=15)),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'db_table': 'reservas',
            },
            bases=('clientes.modelsclientes',),
        ),
    ]

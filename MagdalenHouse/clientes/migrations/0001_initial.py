# Generated by Django 4.2.16 on 2025-02-08 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsClientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_customer', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('last_name_customer', models.CharField(max_length=100, verbose_name='Apellido')),
                ('email_customer', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('phone_customer', models.CharField(max_length=100, verbose_name='Telefono')),
                ('address_customer', models.CharField(max_length=100, verbose_name='Direccion')),
                ('city_customer', models.CharField(max_length=100, verbose_name='Ciudad')),
                ('active_customer', models.BooleanField(default=True, verbose_name='Estado')),
                ('date_create_customer', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'clientes',
            },
        ),
    ]

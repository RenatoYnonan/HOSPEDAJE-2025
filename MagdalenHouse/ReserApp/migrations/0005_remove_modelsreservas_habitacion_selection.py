# Generated by Django 5.1.6 on 2025-02-12 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReserApp', '0004_modelsreservas_departamento_selection_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelsreservas',
            name='habitacion_selection',
        ),
    ]

# Generated by Django 3.2.6 on 2022-11-05 18:32

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20221027_0140'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimientos',
            fields=[
                ('id_manten', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Mantenimiento')),
                ('fecha', models.DateTimeField(blank=True, help_text='Ingrese la fecha de mantenimiento', null=True, verbose_name='Fecha del Mantenimiento')),
                ('descripcion', models.TextField(help_text='Ingrese las observaciones del mantenimiento', verbose_name='Observaciones')),
            ],
        ),


    ]

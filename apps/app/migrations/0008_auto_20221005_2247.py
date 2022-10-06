# Generated by Django 3.2.6 on 2022-10-06 03:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20221005_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(help_text='Ingrese el nombre del empleado', max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_nombre', message='El nombre ingresado no es válido, revise sus espacios o sintaxis', regex='/^[ÁÉÍÓÚA-Z][a-záéíóú]+(\\s+[ÁÉÍÓÚA-Z]?[a-záéíóú]+)*$/')], verbose_name='Nombre del Empleado'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='rfc',
            field=models.CharField(help_text='12-13 caracteres <a href="https://www.sat.gob.mx/consultas/44083/consulta-tu-informacion-fiscal"> consulta tu RFC</a>', max_length=13, validators=[django.core.validators.RegexValidator(code='invalid_RFC', message='El RFC deberá tener el formato que la Servicio de Administración Tributaria valida', regex='^([A-Z][AEIOUX][A-Z]{2}\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])[HM](?:AS|B[CS]|C[CLMSH]|D[FG]|G[TR]|HG|JC|M[CNS]|N[ETL]|OC|PL|Q[TR]|S[PLR]|T[CSL]|VZ|YN|ZS)[B-DF-HJ-NP-TV-Z]{3}[A-Z\\d])(\\d)$')], verbose_name='RFC'),
        ),
    ]
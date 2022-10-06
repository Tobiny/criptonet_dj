# Generated by Django 3.2.6 on 2022-10-06 02:02

import django.core.validators
from django.db import migrations, models
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_producto_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, help_text='Ingrese la descripción del producto', max_length=250, null=True, validators=[django.core.validators.RegexValidator('(^[A-Z][a-zA-ZÀ-ÖØ-öø-ÿ0-9]*[,|.]?(\\s?($|[a-zA-ZÀ-ÖØ-öø-ÿ0-9]+[,|.]?))*)', message='Ingrese una descripción válida.')], verbose_name='Descripción del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='modelo',
            field=models.CharField(blank=True, help_text='Ingrese el modelo del producto', max_length=70, null=True, validators=[django.core.validators.RegexValidator('(^[A-Z][a-zA-ZÀ-ÖØ-öø-ÿ0-9]*[,|.]?(\\s?($|[a-zA-ZÀ-ÖØ-öø-ÿ0-9]+[,|.]?))*)', message='Ingrese una descripción válida.')], verbose_name='Modelo del producto'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=djmoney.models.fields.MoneyField(decimal_places=3, default_currency='MXN', help_text='Ingrese el precio del producto', max_digits=6, max_length=9, validators=[djmoney.models.validators.MinMoneyValidator(0), djmoney.models.validators.MaxMoneyValidator(999999), django.core.validators.RegexValidator('([0-9]*[.])?[0-9]+', message='Ingrese una descripción válida.')], verbose_name='Precio del Producto'),
        ),
    ]

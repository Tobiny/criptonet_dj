# Generated by Django 3.2.6 on 2022-10-27 06:04

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20221026_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='perprice',
        ),
        migrations.AddField(
            model_name='compras',
            name='preciocompra',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='MXN', help_text='Ingrese el precio del producto', max_digits=9, max_length=9, validators=[djmoney.models.validators.MinMoneyValidator(0), djmoney.models.validators.MaxMoneyValidator(999999), django.core.validators.RegexValidator('[0-9]{1,6}([.][0-9]{1,2})?', message='Cantidad de dígitos superada')], verbose_name='Precio del Producto'),
        ),
        migrations.AddField(
            model_name='compras',
            name='preciocompra_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('MXN', 'MXN $'), ('USD', 'USD $')], default='MXN', editable=False, max_length=3),
        ),
        migrations.AddField(
            model_name='compras',
            name='precioventa',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='MXN', help_text='Ingrese el precio del producto', max_digits=9, max_length=9, validators=[djmoney.models.validators.MinMoneyValidator(0), djmoney.models.validators.MaxMoneyValidator(999999), django.core.validators.RegexValidator('[0-9]{1,6}([.][0-9]{1,2})?', message='Cantidad de dígitos superada')], verbose_name='Precio del Producto'),
        ),
        migrations.AddField(
            model_name='compras',
            name='precioventa_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('MXN', 'MXN $'), ('USD', 'USD $')], default='MXN', editable=False, max_length=3),
        ),
    ]

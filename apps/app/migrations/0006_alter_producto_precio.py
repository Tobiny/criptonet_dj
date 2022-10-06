# Generated by Django 3.2.6 on 2022-10-06 02:07

import django.core.validators
from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20221005_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=djmoney.models.fields.MoneyField(decimal_places=3, default_currency='MXN', help_text='Ingrese el precio del producto', max_digits=6, max_length=9, validators=[djmoney.models.validators.MinMoneyValidator(0), djmoney.models.validators.MaxMoneyValidator(999999), django.core.validators.RegexValidator('[0-9]{1-6}([.][0-9]{1-2})?', message='Ingrese una descripción válida.')], verbose_name='Precio del Producto'),
        ),
    ]

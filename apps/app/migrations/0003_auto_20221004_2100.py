# Generated by Django 3.2.6 on 2022-10-05 02:00

from django.db import migrations, models
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20221003_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='numTelefono',
            field=models.CharField(blank=True, help_text='Ingrese el número de teléfono del cliente', max_length=10, null=True, verbose_name='Número de Teléfono'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=djmoney.models.fields.MoneyField(decimal_places=3, default_currency='MXN', help_text='Ingrese el precio del producto', max_digits=6, max_length=9, validators=[djmoney.models.validators.MinMoneyValidator(0), djmoney.models.validators.MaxMoneyValidator(999999)], verbose_name='Precio del Producto'),
        ),
    ]

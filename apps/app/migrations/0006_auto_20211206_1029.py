# Generated by Django 3.2.6 on 2021-12-06 16:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_id_modelo_marca_id_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='id_marca',
            field=models.CharField(help_text='Ingrese la id la marca (p, ej. NVD, AMD,etc.)', max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username must be Alphanumeric', regex='^[a-zA-Z0-9]*3')]),
        ),
        migrations.AlterField(
            model_name='tipoproducto',
            name='id_tipo',
            field=models.CharField(help_text='Ingrese la id tipo de producto (p, ej. TV, PRO)', max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='invalid_id', message='Username must be Alphanumeric', regex='^[a-zA-Z0-9]*3')]),
        ),
    ]

# Generated by Django 3.2.6 on 2021-11-15 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_producto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={'permissions': (('editar_productos', 'Editor de producto'),)},
        ),
    ]
# Generated by Django 3.2.6 on 2021-10-19 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=25)),
                ('precio_venta', models.FloatField(max_length=25)),
                ('existencia', models.IntegerField()),
            ],
        ),
    ]

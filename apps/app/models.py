from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import FloatField, DecimalField, BigAutoField
from djmoney.models.fields import MoneyField


# Create your models here.
class Producto(models.Model):
    id_producto = models.CharField(max_length=14, primary_key=True)
    nom = models.CharField(max_length=120)
    precio_venta = MoneyField(max_length=18, decimal_places=2, max_digits=16)
    cantidad_existente = models.PositiveIntegerField()


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    precio = MoneyField(max_length=18, decimal_places=2, max_digits=16)
    nom = models.CharField(max_length=30)


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Venta', on_delete=models.CASCADE)
    total = MoneyField(max_length=18, decimal_places=2, max_digits=16)
    fecha = models.DateField()


class Mantenimiento(models.Model):
    id_manten = models.AutoField(primary_key=True)
    fecha = models.DateField()
    observaciones = models.TextField()
    tipo_minero = models.CharField(max_length=20, null=True)
    total = MoneyField(max_length=18, decimal_places=2, max_digits=16)


class DetalleMatenimiento(models.Model):
    id_servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    id_manten = models.ForeignKey('Mantenimiento', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = MoneyField(max_length=18, decimal_places=2, max_digits=16)


class DetalleVenta(models.Model):
    id_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True)
    id_venta = models.ForeignKey('Venta', on_delete=models.CASCADE, null=True)
    id_mant = models.ForeignKey('Mantenimiento', on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    subtotal = MoneyField(max_length=18, decimal_places=2, max_digits=16)


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    nom = models.CharField(max_length=50, help_text="Ingrese el nombre del cliente")
    dom = models.CharField(max_length=100, help_text="Ingrese el domicilio del cliente")
    mail = models.EmailField(max_length=254)
    rfc = models.CharField(max_length=13, help_text='12-13 caracteres<a href="https://www.sat.gob.mx/consultas/44083'
                                                    '/consulta-tu-informacion-fiscal '
                                                    '">consulta tu RFC</a>')


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50, help_text="Ingrese el nombre del empleado")
    rfc = models.CharField(max_length=50, help_text="Ingrese el rfc del empleado")

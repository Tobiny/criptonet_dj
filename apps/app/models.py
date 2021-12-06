import uuid

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from djmoney.models.fields import MoneyField


# Create your models here.
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True, verbose_name='ID Empleado')
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del empleado", verbose_name='Nombre del '
                                                                                                      'Empleado')
    rfc = models.CharField(max_length=50, help_text="Ingrese el rfc del empleado", verbose_name='RFC')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s' % self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Producto
        """
        return reverse('empleado_detalles', args=[str(self.id_empleado)])


class Marca(models.Model):
    id_marca = models.CharField(primary_key=True, max_length=3, verbose_name='ID Marca',
                                help_text="Ingrese la id la marca (p, ej. NVD, AMD,"
                                          "etc.)", validators=[RegexValidator(
            regex='^([A-Z0-9]){3}',
            message='La id debe ser de 3 dígitos y debe tener solo letras mayúsculas y números',
            code='invalid_id_marca'), ])
    nombre = models.CharField(verbose_name='Nombre de Marca', max_length=200,
                              help_text="Ingrese la marca (p. ej. AMD,Nvidia, etc)")

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s' % self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Producto
        """
        return reverse('marca_detalles', args=[str(self.id_marca)])


class TipoProducto(models.Model):
    id_tipo = models.CharField(primary_key=True, verbose_name='ID del Tipo', max_length=3,
                               help_text="Ingrese la id tipo de producto (p, ej. TV, "
                                         "PRO)", validators=[RegexValidator(
            regex='^([A-Z0-9]){3}',
            message='La id debe ser de 3 dígitos y debe tener solo letras mayúsculas y números',
            code='invalid_id'), ])
    nombre = models.CharField(verbose_name='Nombre del Tipo', max_length=200,
                              help_text="Ingrese el tipo de producto (p. ej. Tarjeta de video, Procesador etc.)")

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s' % self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Producto
        """
        return reverse('tipo_detalles', args=[str(self.id_tipo)])


class Producto(models.Model):
    id_producto = models.UUIDField(primary_key=True, verbose_name='ID de Producto', default=uuid.uuid4,
                                   help_text="ID único generado para este producto "
                                             "particular en toda la tienda")

    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, help_text="Seleccione el tipo de producto.")
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, help_text="Seleccione la marca del producto.")
    modelo = models.CharField(max_length=120, verbose_name='Modelo de Producto', help_text="Ingrese el modelo del "
                                                                                           "producto (p. ej. Ryzen "
                                                                                           "3600X, GeForce "
                                                                                           "1660 Super, etc.)")
    precio_venta = MoneyField(verbose_name='Precio a la venta', max_length=18, decimal_places=2, max_digits=16,
                              help_text="Ingrese el precio del producto con su tipo de moneda.", default_currency='MXN')
    cantidad_existente = models.PositiveIntegerField(verbose_name='Cantidad de Productos',
                                                     help_text="Ingrese la cantidad de producto a añadir o modificar.")

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s-(%s)' % (self.id_producto[:4], self.modelo)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Producto
        """
        return reverse('producto_detalles', args=[str(self.id_producto)])


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True, verbose_name='ID de Servicio')
    precio = MoneyField(verbose_name='Precio del Servicio', max_length=18, decimal_places=2, max_digits=16,
                        default_currency='MXN',
                        help_text="Ingrese el costo del servicio")
    nombre = models.CharField(max_length=30, help_text="Ingrese el nombre del servicio.", verbose_name='Nombre del '
                                                                                                       'Servicio')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s' % self.nombre


class Mantenimiento(models.Model):
    id_manten = models.AutoField(primary_key=True, verbose_name='ID del Mantenimiento')
    fecha = models.DateField(verbose_name='Fecha del Mantenimiento')
    observaciones = models.TextField(help_text="Ingrese las observaciones del mantenimiento",
                                     verbose_name='Observaciones')
    tipo_minero = models.CharField(max_length=20, help_text="Ingrese el tipo de minero (puede estár vacio)", null=True,
                                   verbose_name='Tipo de Minero')
    total = MoneyField(max_length=18, decimal_places=2, max_digits=16, verbose_name='Total')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s - %s' % (self.id_manten, self.fecha)


class DetalleMatenimiento(models.Model):
    id_servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE)
    id_manten = models.ForeignKey('Mantenimiento', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = MoneyField(max_length=18, decimal_places=2, max_digits=16)

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s - %s' % (self.id_manten.id_manten, self.id_servicio.nombre)


class DetalleVenta(models.Model):
    id_producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, blank=True)
    id_venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    id_manten = models.ForeignKey('Mantenimiento', on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField()
    subtotal = MoneyField(max_length=18, decimal_places=2, max_digits=16)

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s - %s' % (self.id_venta.id_venta, self.id_venta.fecha)


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name='ID Cliente')
    id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del cliente")
    domicilio = models.CharField(max_length=100, help_text="Ingrese el domicilio del cliente")
    mail = models.EmailField(max_length=254, help_text="Ingrese el correo del cliente", verbose_name='Correo Cliente')
    RFC = models.CharField(max_length=13, help_text='12-13 caracteres <a href="https://www.sat.gob.mx/consultas/44083'
                                                    '/consulta-tu-informacion-fiscal '
                                                    '"> consulta tu RFC</a>')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s - %s' % (self.nombre, self.RFC[:5])


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True, verbose_name='ID Venta')
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    total = MoneyField(max_length=18, decimal_places=2, max_digits=16)
    fecha = models.DateField()

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s - %s' % (self.id_venta, self.id_cliente.nombre)

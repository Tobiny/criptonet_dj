from uuid import uuid4

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
from django.forms import DateInput
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from djmoney.models.fields import MoneyField


# Create your models here.
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True, verbose_name='ID Empleado')
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del empleado", verbose_name='Nombre del '
                                                                                                      'Empleado')
    rfc = models.CharField(max_length=13, verbose_name='RFC', help_text='12-13 caracteres <a '
                                                                        'href="https://www.sat.gob.mx/consultas/44083 '
                                                                        '/consulta-tu-informacion-fiscal '
                                                                        '"> consulta tu RFC</a>',
                           validators=[RegexValidator(
                               regex='^([A-ZÑ\x26]{3,4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1]))((-)?([A-Z\d]{3}))?$',
                               message='El RFC deberá tener el formato que la Servicio de Administración Tributaria valida',
                               code='invalid_RFC'), ])

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
        return '%s - %s' % (self.nombre, self.precio)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Producto
        """
        return reverse('servicio_detalles', args=[str(self.id_servicio)])


class Mantenimiento(models.Model):
    id_manten = models.AutoField(primary_key=True, verbose_name='ID del Mantenimiento')
    id_servicio = models.ForeignKey('Servicio', on_delete=models.CASCADE, null=False)

    cantidad_servicios = models.IntegerField('Cantidad de servicios', validators=[MinValueValidator(1)])
    fecha = models.DateField(verbose_name='Fecha del Mantenimiento')
    observaciones = models.TextField(help_text="Ingrese las observaciones del mantenimiento",
                                     verbose_name='Observaciones')

    total = MoneyField(max_length=18, decimal_places=2, max_digits=16, verbose_name='Total', editable=False)

    def save(self, *args, **kwargs):
        self.total = self.id_servicio.precio * self.cantidad_servicios
        super(Mantenimiento, self).save(*args, **kwargs)

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s - %s' % (self.id_manten, self.fecha)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Producto
        """
        return reverse('mantenimiento_detalles', args=[str(self.id_manten)])


class DetalleVenta(models.Model):
    productos = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True, blank=True)
    id_venta = models.ForeignKey('Venta', on_delete=models.CASCADE)
    id_manten = models.ForeignKey('Mantenimiento', on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField()
    subtotal = MoneyField(max_length=18, decimal_places=2, max_digits=16)

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s - %s' % (self.id_venta.id_venta, self.id_venta.fecha)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Producto
        """
        return reverse('mantenimiento_detalles', args=[str(self.id_venta)])


class Cliente(models.Model):
    ESTADOS = [
        ("Aguascalientes'", "Aguascalientes"),
        ("Baja California", "Baja California"),
        ("Baja California Sur", "Baja California Sur"),
        ("Campeche", "Campeche"),
        ("Chiapas", "Chiapas"),
        ("Chihuahua", "Chihuahua"),
        ("Ciudad de México", "Ciudad de México"),
        ("Coahuila", "Coahuila"),
        ("Colima", "Colima"),
        ("Durango", "Durango"),
        ("Guanajuato", "Guanajuato"),
        ("Guerrero", "Guerrero"),
        ("Hidalgo", "Hidalgo"),
        ("Jalisco", "Jalisco"),
        ("México", "México"),
        ("Michoacán", "Michoacán"),
        ("Morelos", "Morelos"),
        ("Nayarit", "Nayarit"),
        ("Nuevo León", "Nuevo León"),
        ("Oaxaca", "Oaxaca"),
        ("Puebla", "Puebla"),
        ("Querétaro", "Querétaro"),
        ("Quintana Roo", "Quintana Roo"),
        ("San Luis Potosí", "San Luis Potosí"),
        ("Sinaloa", "Sinaloa"),
        ("Sonora", "Sonora"),
        ("Tabasco", "Tabasco"),
        ("Tamaulipas", "Tamaulipas"),
        ("Tlaxcala", "Tlaxcala"),
        ("Veracruz", "Veracruz"),
        ("Yucatán", "Yucatán"),
        ("Zacatecas", "Zacatecas"),
    ]

    # Basic Fields.
    nombreCliente = models.CharField(null=True, blank=True, max_length=200)
    domicilio = models.CharField(null=True, blank=True, max_length=200)
    estado = models.CharField(choices=ESTADOS, blank=True, default="Jalisco", max_length=100)
    codigoPostal = models.CharField(null=True, blank=True, max_length=10)
    numTelefono = models.CharField(null=True, blank=True, max_length=100)
    dirEmail = models.CharField(null=True, blank=True, max_length=100)
    rfcCliente = models.CharField(null=True, blank=True, max_length=100, validators=[RegexValidator(
        regex='^([A-ZÑ\x26]{3,4}([0-9]{2})(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1]))((-)?([A-Z\d]{3}))?$',
        message='El RFC deberá tener el formato que la Servicio de Administración Tributaria valida',
        code='invalid_RFC2'), ])

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {} {}'.format(self.nombreCliente, self.estado, self.uniqueId)

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.nombreCliente, self.estado, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.nombreCliente, self.estado, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Cliente, self).save(*args, **kwargs)


class Recibo(models.Model):
    TERMS = [
        ('14 días', '14 días'),
        ('30 días', '30 días'),
        ('60 días', '60 días'),
    ]

    STATUS = [
        ('ACTUAL', 'ACTUAL'),
        ('NO PAGADO', 'NO PAGADO'),
        ('PAGADO', 'PAGADO'),
    ]

    title = models.CharField(null=True, blank=True, max_length=100)
    numero = models.CharField(null=True, blank=True, max_length=100)
    fechaPago = models.DateField(null=True, blank=True)
    terminosPago = models.CharField(choices=TERMS, default='14 days', max_length=100)
    estado = models.CharField(choices=STATUS, default='CURRENT', max_length=100)
    notas = models.TextField(null=True, blank=True)

    # RELATED fields
    cliente = models.ForeignKey(Cliente, blank=True, null=True, on_delete=models.SET_NULL)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.numero, self.uniqueId)

    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.numero, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.numero, self.uniqueId))
        self.ultima_actualizacion = timezone.localtime(timezone.now())

        super(Recibo, self).save(*args, **kwargs)


class Producto(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    cantidad = models.FloatField(null=True, blank=True)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE, default='Sin tipo')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default='Sin marca')
    precio = MoneyField(max_length=30, decimal_places=3, max_digits=27,
                        default_currency='MXN')
    uniqueId = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        super(Producto, self).save(*args, **kwargs)


class DetalleProducto(models.Model):
    # Related Fields
    producto = models.ForeignKey(Producto, blank=True, null=True, on_delete=models.CASCADE)
    recibo = models.ForeignKey(Recibo, blank=True, null=True, on_delete=models.CASCADE)
    cantidad = models.FloatField(null=False)
    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.uniqueId)

    def get_absolute_url(self):
        return reverse('venta-detail', kwargs={'slug': self.slug})

    def clean(self):
        # Don't allow draft entries to have a pub_date.
        if self.producto.cantidad < self.cantidad:
            raise ValidationError({'cantidad': ('La cantidad de productos a comprar debe ser menor a la que hay en '
                                                'inventario')})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.producto.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.producto.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(DetalleProducto, self).save(*args, **kwargs)



class Settings(models.Model):
    ESTADOS = [
        ("Aguascalientes'", "Aguascalientes"),
        ("Baja California", "Baja California"),
        ("Baja California Sur", "Baja California Sur"),
        ("Campeche", "Campeche"),
        ("Chiapas", "Chiapas"),
        ("Chihuahua", "Chihuahua"),
        ("Ciudad de México", "Ciudad de México"),
        ("Coahuila", "Coahuila"),
        ("Colima", "Colima"),
        ("Durango", "Durango"),
        ("Guanajuato", "Guanajuato"),
        ("Guerrero", "Guerrero"),
        ("Hidalgo", "Hidalgo"),
        ("Jalisco", "Jalisco"),
        ("México", "México"),
        ("Michoacán", "Michoacán"),
        ("Morelos", "Morelos"),
        ("Nayarit", "Nayarit"),
        ("Nuevo León", "Nuevo León"),
        ("Oaxaca", "Oaxaca"),
        ("Puebla", "Puebla"),
        ("Querétaro", "Querétaro"),
        ("Quintana Roo", "Quintana Roo"),
        ("San Luis Potosí", "San Luis Potosí"),
        ("Sinaloa", "Sinaloa"),
        ("Sonora", "Sonora"),
        ("Tabasco", "Tabasco"),
        ("Tamaulipas", "Tamaulipas"),
        ("Tlaxcala", "Tlaxcala"),
        ("Veracruz", "Veracruz"),
        ("Yucatán", "Yucatán"),
        ("Zacatecas", "Zacatecas"),
    ]

    # Basic Fields
    clientName = models.CharField(null=True, blank=True, max_length=200)
    addressLine1 = models.CharField(null=True, blank=True, max_length=200)
    province = models.CharField(choices=ESTADOS, blank=True, max_length=100)
    postalCode = models.CharField(null=True, blank=True, max_length=10)
    phoneNumber = models.CharField(null=True, blank=True, max_length=100)
    emailAddress = models.CharField(null=True, blank=True, max_length=100)
    taxNumber = models.CharField(null=True, blank=True, max_length=100)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {} {}'.format(self.clientName, self.province, self.uniqueId)

    def get_absolute_url(self):
        return reverse('settings-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))

        self.slug = slugify('{} {} {}'.format(self.clientName, self.province, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(Settings, self).save(*args, **kwargs)


class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True, verbose_name='ID Venta')
    id_empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    id_cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    total = MoneyField(max_length=18, decimal_places=2, max_digits=16)
    fecha = models.DateField()

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s - %s' % (self.id_venta, self.id_cliente.nombre)

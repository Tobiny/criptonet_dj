from uuid import uuid4

from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from djmoney.models.fields import MoneyField
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator


# Create your models here.
class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True, verbose_name='ID Empleado')
    nombre = models.CharField(max_length=50, help_text="Ingrese el nombre del empleado", verbose_name='Nombre del '
                                                                                                      'Empleado',
                              validators=[RegexValidator(
                                  regex='^[ÁÉÍÓÚA-Z][a-záéíóú]*(\s[ÁÉÍÓÚA-Z][a-záéíóú]*)*',
                                  message='El nombre ingresado no es válido, revise sus espacios o sintaxis',
                                  code='invalid_nombre'), ])
    rfc = models.CharField(max_length=13, verbose_name='RFC',
                           help_text=mark_safe(
                               '12-13 caracteres <a href="https://www.sat.gob.mx/consultas/44083/consulta-tu-informacion-fiscal"> consulta tu RFC</a>'),
                           validators=[RegexValidator(
                               regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$',
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


class Mantenimiento(models.Model):
    id_manten = models.AutoField(primary_key=True, verbose_name='ID del Mantenimiento')
    fechaIngreso = models.DateField(verbose_name='Fecha del Mantenimiento')
    fechaTermina = models.DateField(verbose_name='Fecha del Mantenimiento')
    descripcion = models.TextField(help_text="Ingrese las observaciones del mantenimiento",
                                   verbose_name='Observaciones')

    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s - %s' % (self.id_manten, self.fechaIngreso)

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Producto
        """
        return reverse('mantenimiento_detalles', args=[str(self.id_manten)])


class Client(models.Model):
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
    nombreCliente = models.CharField(null=True, blank=True, max_length=50, help_text="Ingrese el nombre del cliente",
                                     verbose_name='Nombre del '
                                                  'Cliente', validators=[RegexValidator(
            regex='^[ÁÉÍÓÚA-Z][a-záéíóú]*(\s[ÁÉÍÓÚA-Z][a-záéíóú]*)*',
            message='El nombre ingresado no es válido, revise sus espacios o sintaxis',
            code='invalid_nombre')])
    domicilio = models.CharField(null=True, blank=True, max_length=50, help_text="Ingrese el domicilio del cliente",
                                 verbose_name='Domicilio del '
                                              'Cliente')
    estado = models.CharField(choices=ESTADOS, blank=True, default="Jalisco", max_length=20,
                              help_text="Ingrese el estado", verbose_name='Estado'
                              )
    codigoPostal = models.IntegerField(null=True, blank=True, max_length=5,
                                       help_text="Ingrese el codigo postal del cliente",
                                       verbose_name='Codigo Postal del '
                                                    'Cliente',
                                       validators=[RegexValidator(
                                           regex='\d{5}',
                                           message='Código postal inválido',
                                           code='invalid_PC'), ])

    numTelefono = models.CharField(null=True, blank=True, max_length=10,
                                   help_text="Ingrese el número de teléfono del cliente", verbose_name='Número de '
                                                                                                       'Teléfono',
                                   validators=[RegexValidator(
                                       regex='(\(\d{3}\)[.-]?|\d{3}[.-]?)?\d{3}[.-]?\d{4}',
                                       message='El número es inválido.',
                                       code='invalid_number'), ])
    dirEmail = models.EmailField(null=True, blank=True, max_length=100,
                                 help_text="Ingrese la dirección de correo del cliente", verbose_name='Email del '
                                                                                                      'Cliente',
                                 validators=[RegexValidator(
                                     regex='[a-z0-9]+@[a-z]+\.[a-z]{2,3}',
                                     message='El correo es inválido.',
                                     code='invalid_email'), ])
    rfcCliente = models.CharField(null=True, blank=True, max_length=13, validators=[RegexValidator(
        regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$',
        message='El RFC deberá tener el formato que la Servicio de Administración Tributaria valida',
        code='invalid_RFC'), ])

    # Utility fields
    uniqueId = models.UUIDField(primary_key=True, editable=False, verbose_name='ID del Cliente', default=uuid4,
                                help_text="ID único generado para este cliente "
                                          "particular en toda la tienda")
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True, editable=False)
    date_created = models.DateTimeField(blank=True, null=True, editable=False)
    last_updated = models.DateTimeField(blank=True, null=True, editable=False)

    def __str__(self):
        return '{} {} {}'.format(self.nombreCliente, self.estado, self.uniqueId)

    def get_absolute_url(self):
        return reverse('cliente_detalles', args=[str(self.uniqueId)])

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())

        temp = str(uuid4()).split('-')[4]
        self.slug = slugify('{} {} {}'.format(self.nombreCliente, self.estado, temp))
        self.last_updated = timezone.localtime(timezone.now())

        super(Client, self).save(*args, **kwargs)


# contains the sale bills made
class SaleBill(models.Model):
    billno = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)
    notas = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Bill no: " + str(self.billno)

    def get_items_list(self):
        return SaleItem.objects.filter(billno=self)

    def get_total_price(self):
        saleitems = SaleItem.objects.filter(billno=self)
        total = 0
        for item in saleitems:
            total += item.totalprice
        return total


class Recibo(models.Model):
    STATUS = [
        ('ACTUAL', 'ACTUAL'),
        ('NO PAGADO', 'NO PAGADO'),
        ('PAGADO', 'PAGADO'),
    ]

    title = models.CharField(null=True, blank=True, max_length=100, help_text="Ingrese el título del recibo",
                             verbose_name='Título del '
                                          'Recibo')
    numero = models.CharField(null=True, blank=True, max_length=100)
    fechaPago = models.DateField(null=True, blank=True)

    estado = models.CharField(choices=STATUS, default='CURRENT', max_length=100)
    notas = models.TextField(null=True, blank=True)
    total = MoneyField(max_length=30, default=0, decimal_places=3, max_digits=27,
                       default_currency='MXN')

    # RELATED fields
    client = models.ForeignKey(Client, blank=True, null=True, on_delete=models.SET_NULL)

    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.numero, self.uniqueId)

    def actualizar_total(self, x):
        self.total = self.total + (x)

    def get_absolute_url(self):
        return reverse('invoice-detail', kwargs={'slug': self.slug})

    def get_items_list(self):
        return DetalleProducto.objects.filter(recibo=self)

    def get_total_price(self):
        saleitems = DetalleProducto.objects.filter(recibo=self)
        total = 0
        for item in saleitems:
            total += item.preciototal
        return total

    def save(self, *args, **kwargs):
        if self.fecha_creacion is None:
            self.fecha_creacion = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.numero, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.numero, self.uniqueId))
        self.ultima_actualizacion = timezone.localtime(timezone.now())

        super(Recibo, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super(Recibo, self).delete(*args, **kwargs)


class Producto(models.Model):
    modelo = models.CharField(null=True, blank=True, max_length=70, verbose_name='Modelo del producto',
                              help_text='Ingrese el modelo del producto')
    descripcion = models.TextField(null=True, blank=True, help_text="Ingrese la descripción del producto",
                                   verbose_name='Descripción'
                                                ' del producto', max_length=250,

                                   )
    cantidad = models.IntegerField(null=True, blank=True,
                                   help_text="Ingrese la cantidad de productos en existencia/añadir",
                                   verbose_name='Cantidad de '
                                                'Productos en Existencia', max_length=6, default=0)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE,
                                      help_text="Seleccione el tipo de producto", verbose_name='Tipo de producto'
                                      , default='Sin tipo')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default='Sin marca',
                              help_text="Ingrese la marca del producto", verbose_name='Marca del '
                                                                                      'Producto')
    precioCompra = MoneyField(decimal_places=2, max_digits=9, max_length=9, default=0,
                              default_currency='MXN', help_text="Ingrese el precio del producto",
                              verbose_name='Precio del Producto', validators=[MinMoneyValidator(0),
                                                                              MaxMoneyValidator(999999), RegexValidator(
                '[0-9]{1,6}([.][0-9]{1,2})?',
                message="Cantidad de dígitos superada")])

    precioVenta = MoneyField(decimal_places=2, max_digits=9, max_length=9, default=0,
                             default_currency='MXN', help_text="Ingrese el precio del producto",
                             verbose_name='Precio del Producto', validators=[MinMoneyValidator(0),
                                                                             MaxMoneyValidator(999999), RegexValidator(
                '[0-9]{1,6}([.][0-9]{1,2})?',
                message="Cantidad de dígitos superada")])

    uniqueId = models.UUIDField(primary_key=True, editable=False, verbose_name='ID de Producto', default=uuid4,
                                help_text="ID único generado para este producto "
                                          "particular en toda la tienda")
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True, editable=False)

    def __str__(self):
        return '{} {}'.format(self.modelo, self.uniqueId)

    def sumar(self, x):
        self.cantidad += x

    def restar(self, x):
        self.cantidad = self.cantidad - x

    def get_absolute_url(self):
        return reverse('producto_detalles', args=[str(self.uniqueId)])

    def save(self, *args, **kwargs):
        self.slug = slugify('{} {}'.format(self.marca.id_marca, self.uniqueId))

        super(Producto, self).save(*args, **kwargs)


class DetalleProducto(models.Model):
    # Related Fields
    producto = models.ForeignKey(Producto, blank=True, null=True, on_delete=models.CASCADE)
    recibo = models.ForeignKey(Recibo, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.FloatField(null=False)
    subtotal = MoneyField(max_length=30, decimal_places=3, max_digits=27,
                          default_currency='MXN', default=0)
    preciototal = MoneyField(max_length=30, decimal_places=3, max_digits=27,
                             default_currency='MXN', default=0)
    # Utility fields
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    creacion = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.uniqueId)

    def get_absolute_url(self):
        return reverse('venta-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.producto.modelo, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.producto.modelo, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(DetalleProducto, self).save(*args, **kwargs)


class SaleItem(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete=models.CASCADE, related_name='salebillno')
    stock = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='saleitem')
    quantity = models.IntegerField(default=1)
    perprice = models.FloatField(default=1)
    totalprice = models.FloatField(default=1)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno) + ", Item = " + self.stock.modelo


# contains the other details in the sales bill
class SaleBillDetails(models.Model):
    billno = models.ForeignKey(SaleBill, on_delete=models.CASCADE, related_name='saledetailsbillno')

    eway = models.CharField(max_length=50, blank=True, null=True)
    veh = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)

    cgst = models.CharField(max_length=50, blank=True, null=True)
    sgst = models.CharField(max_length=50, blank=True, null=True)
    igst = models.CharField(max_length=50, blank=True, null=True)
    cess = models.CharField(max_length=50, blank=True, null=True)
    tcs = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Bill no: " + str(self.billno.billno)


# contains the purchase bills made
class ReciboCompra(models.Model):
    billno = models.AutoField(primary_key=True)
    notas = models.TextField(null=True, blank=True, help_text="Ingrese algún mensaje de ayuda para un mejor control")
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Número de recibo: " + str(self.billno)

    def get_items_list(self):
        return Compras.objects.filter(billno=self)

    def get_total_price(self):
        articuloscomprados = Compras.objects.filter(billno=self)
        total = 0
        for item in articuloscomprados:
            total += item.totalprice
        return total


# contains the purchase stocks made
class Compras(models.Model):
    billno = models.ForeignKey(ReciboCompra, on_delete=models.CASCADE, related_name='purchasebillno')
    stock = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='purchaseitem')
    quantity = models.IntegerField(default=1, help_text="Ingrese la cantidad de productos a comprar")
    preciocompra = MoneyField(decimal_places=2, max_digits=9, max_length=9, default=1,
                              default_currency='MXN', help_text="Ingrese el precio del producto",
                              verbose_name='Precio del Producto', validators=[MinMoneyValidator(0),
                                                                              MaxMoneyValidator(999999), RegexValidator(
                '[0-9]{1,6}([.][0-9]{1,2})?',
                message="Cantidad de dígitos superada")])
    precioventa = MoneyField(decimal_places=2, max_digits=9, max_length=9, default=1,
                             default_currency='MXN', help_text="Ingrese el precio del producto",
                             verbose_name='Precio del Producto', validators=[MinMoneyValidator(0),
                                                                             MaxMoneyValidator(999999), RegexValidator(
                '[0-9]{1,6}([.][0-9]{1,2})?',
                message="Cantidad de dígitos superada")])
    totalprice = MoneyField(decimal_places=2, max_digits=9, max_length=9, default=0,
                             default_currency='MXN', help_text="Ingrese el precio del producto",
                             verbose_name='Precio total', validators=[MinMoneyValidator(0),
                                                                             MaxMoneyValidator(999999), RegexValidator(
                '[0-9]{1,6}([.][0-9]{1,2})?',
                message="Cantidad de dígitos superada")])

    def __str__(self):
        return "Número de recibo " + str(self.billno.billno) + ", Artículo = " + self.stock.name


# contains the other details in the purchases bill
class DetallesReciboCompra(models.Model):
    billno = models.ForeignKey(ReciboCompra, on_delete=models.CASCADE, related_name='purchasedetailsbillno')

    eway = models.CharField(max_length=50, blank=True, null=True)
    veh = models.CharField(max_length=50, blank=True, null=True)
    destino = models.CharField(max_length=50, blank=True, null=True)
    po = models.CharField(max_length=50, blank=True, null=True)

    cgst = models.CharField(max_length=50, blank=True, null=True)
    sgst = models.CharField(max_length=50, blank=True, null=True)
    igst = models.CharField(max_length=50, blank=True, null=True)
    cess = models.CharField(max_length=50, blank=True, null=True)
    tcs = models.CharField(max_length=50, blank=True, null=True)
    total = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Número de recibo: " + str(self.billno.billno)

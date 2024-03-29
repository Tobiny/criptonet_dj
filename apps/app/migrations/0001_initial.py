# Generated by Django 3.2.6 on 2022-10-07 19:05

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields
import djmoney.models.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('nombreCliente', models.CharField(blank=True, help_text='Ingrese el nombre del cliente', max_length=50, null=True, validators=[django.core.validators.RegexValidator(code='invalid_nombre', message='El nombre ingresado no es válido, revise sus espacios o sintaxis', regex='^[ÁÉÍÓÚA-Z][a-záéíóú]*(\\s[ÁÉÍÓÚA-Z][a-záéíóú]*)*')], verbose_name='Nombre del Cliente')),
                ('domicilio', models.CharField(blank=True, help_text='Ingrese el domicilio del cliente', max_length=50, null=True, verbose_name='Domicilio del Cliente')),
                ('estado', models.CharField(blank=True, choices=[("Aguascalientes'", 'Aguascalientes'), ('Baja California', 'Baja California'), ('Baja California Sur', 'Baja California Sur'), ('Campeche', 'Campeche'), ('Chiapas', 'Chiapas'), ('Chihuahua', 'Chihuahua'), ('Ciudad de México', 'Ciudad de México'), ('Coahuila', 'Coahuila'), ('Colima', 'Colima'), ('Durango', 'Durango'), ('Guanajuato', 'Guanajuato'), ('Guerrero', 'Guerrero'), ('Hidalgo', 'Hidalgo'), ('Jalisco', 'Jalisco'), ('México', 'México'), ('Michoacán', 'Michoacán'), ('Morelos', 'Morelos'), ('Nayarit', 'Nayarit'), ('Nuevo León', 'Nuevo León'), ('Oaxaca', 'Oaxaca'), ('Puebla', 'Puebla'), ('Querétaro', 'Querétaro'), ('Quintana Roo', 'Quintana Roo'), ('San Luis Potosí', 'San Luis Potosí'), ('Sinaloa', 'Sinaloa'), ('Sonora', 'Sonora'), ('Tabasco', 'Tabasco'), ('Tamaulipas', 'Tamaulipas'), ('Tlaxcala', 'Tlaxcala'), ('Veracruz', 'Veracruz'), ('Yucatán', 'Yucatán'), ('Zacatecas', 'Zacatecas')], default='Jalisco', help_text='Ingrese el estado', max_length=20, verbose_name='Estado')),
                ('codigoPostal', models.IntegerField(blank=True, help_text='Ingrese el codigo postal del cliente', max_length=5, null=True, validators=[django.core.validators.RegexValidator(code='invalid_PC', message='Código postal inválido', regex='\\d{5}')], verbose_name='Codigo Postal del Cliente')),
                ('numTelefono', models.CharField(blank=True, help_text='Ingrese el número de teléfono del cliente', max_length=10, null=True, validators=[django.core.validators.RegexValidator(code='invalid_number', message='El número es inválido.', regex='(\\(\\d{3}\\)[.-]?|\\d{3}[.-]?)?\\d{3}[.-]?\\d{4}')], verbose_name='Número de Teléfono')),
                ('dirEmail', models.EmailField(blank=True, help_text='Ingrese la dirección de correo del cliente', max_length=100, null=True, validators=[django.core.validators.RegexValidator(code='invalid_email', message='El correo es inválido.', regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])) ?(?:- ?)?([A-Z\\d]{2})([A\\d])$')], verbose_name='Email del Cliente')),
                ('rfcCliente', models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(code='invalid_RFC', message='El RFC deberá tener el formato que la Servicio de Administración Tributaria valida', regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])) ?(?:- ?)?([A-Z\\d]{2})([A\\d])$')])),
                ('uniqueId', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID único generado para este cliente particular en toda la tienda', primary_key=True, serialize=False, verbose_name='ID del Cliente')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, editable=False, null=True)),
                ('last_updated', models.DateTimeField(blank=True, editable=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Empleado')),
                ('nombre', models.CharField(help_text='Ingrese el nombre del empleado', max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_nombre', message='El nombre ingresado no es válido, revise sus espacios o sintaxis', regex='^[ÁÉÍÓÚA-Z][a-záéíóú]*(\\s[ÁÉÍÓÚA-Z][a-záéíóú]*)*')], verbose_name='Nombre del Empleado')),
                ('rfc', models.CharField(help_text='12-13 caracteres <a href="https://www.sat.gob.mx/consultas/44083/consulta-tu-informacion-fiscal"> consulta tu RFC</a>', max_length=13, validators=[django.core.validators.RegexValidator(code='invalid_RFC', message='El RFC deberá tener el formato que la Servicio de Administración Tributaria valida', regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\\d|3[01])) ?(?:- ?)?([A-Z\\d]{2})([A\\d])$')], verbose_name='RFC')),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id_manten', models.AutoField(primary_key=True, serialize=False, verbose_name='ID del Mantenimiento')),
                ('fechaIngreso', models.DateField(verbose_name='Fecha del Mantenimiento')),
                ('fechaTermina', models.DateField(verbose_name='Fecha del Mantenimiento')),
                ('descripcion', models.TextField(help_text='Ingrese las observaciones del mantenimiento', verbose_name='Observaciones')),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id_marca', models.CharField(help_text='Ingrese la id la marca (p, ej. NVD, AMD,etc.)', max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='invalid_id_marca', message='La id debe ser de 3 dígitos y debe tener solo letras mayúsculas y números', regex='^([A-Z0-9]){3}')], verbose_name='ID Marca')),
                ('nombre', models.CharField(help_text='Ingrese la marca (p. ej. AMD,Nvidia, etc)', max_length=200, verbose_name='Nombre de Marca')),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo', models.CharField(help_text='Ingrese la id tipo de producto (p, ej. TV, PRO)', max_length=3, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator(code='invalid_id', message='La id debe ser de 3 dígitos y debe tener solo letras mayúsculas y números', regex='^([A-Z0-9]){3}')], verbose_name='ID del Tipo')),
                ('nombre', models.CharField(help_text='Ingrese el tipo de producto (p. ej. Tarjeta de video, Procesador etc.)', max_length=200, verbose_name='Nombre del Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Ingrese el título del recibo', max_length=100, null=True, verbose_name='Título del Recibo')),
                ('numero', models.CharField(blank=True, max_length=100, null=True)),
                ('fechaPago', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('ACTUAL', 'ACTUAL'), ('NO PAGADO', 'NO PAGADO'), ('PAGADO', 'PAGADO')], default='CURRENT', max_length=100)),
                ('notas', models.TextField(blank=True, null=True)),
                ('total_currency', djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('MXN', 'MXN $'), ('USD', 'USD $')], default='MXN', editable=False, max_length=3)),
                ('total', djmoney.models.fields.MoneyField(decimal_places=3, default=Decimal('0'), default_currency='MXN', max_digits=27, max_length=30)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('fecha_creacion', models.DateTimeField(blank=True, null=True)),
                ('ultima_actualizacion', models.DateTimeField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.client')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('modelo', models.CharField(blank=True, help_text='Ingrese el modelo del producto', max_length=70, null=True, verbose_name='Modelo del producto')),
                ('descripcion', models.TextField(blank=True, help_text='Ingrese la descripción del producto', max_length=250, null=True, verbose_name='Descripción del producto')),
                ('cantidad', models.FloatField(blank=True, default=0, help_text='Ingrese la cantidad de productos en existencia/añadir', max_length=6, null=True, verbose_name='Cantidad de Productos en Existencia')),
                ('precio_currency', djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('MXN', 'MXN $'), ('USD', 'USD $')], default='MXN', editable=False, max_length=3)),
                ('precio', djmoney.models.fields.MoneyField(decimal_places=2, default_currency='MXN', help_text='Ingrese el precio del producto', max_digits=9, max_length=9, validators=[djmoney.models.validators.MinMoneyValidator(0), djmoney.models.validators.MaxMoneyValidator(999999), django.core.validators.RegexValidator('[0-9]{1,6}([.][0-9]{1,2})?', message='Cantidad de dígitos superada')], verbose_name='Precio del Producto')),
                ('uniqueId', models.UUIDField(default=uuid.uuid4, editable=False, help_text='ID único generado para este producto particular en toda la tienda', primary_key=True, serialize=False, verbose_name='ID de Producto')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=500, null=True, unique=True)),
                ('marca', models.ForeignKey(default='Sin marca', help_text='Ingrese la marca del producto', on_delete=django.db.models.deletion.CASCADE, to='app.marca', verbose_name='Marca del Producto')),
                ('tipo_producto', models.ForeignKey(default='Sin tipo', help_text='Seleccione el tipo de producto', on_delete=django.db.models.deletion.CASCADE, to='app.tipoproducto', verbose_name='Tipo de producto')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField()),
                ('subtotal_currency', djmoney.models.fields.CurrencyField(choices=[('EUR', 'EUR €'), ('MXN', 'MXN $'), ('USD', 'USD $')], default='MXN', editable=False, max_length=3)),
                ('subtotal', djmoney.models.fields.MoneyField(decimal_places=3, default_currency='MXN', max_digits=27, max_length=30)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('creacion', models.IntegerField(blank=True, null=True)),
                ('producto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
                ('recibo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.recibo')),
            ],
        ),
    ]

from django.contrib import admin

# Register your models here.
from apps.app.models import *

admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Venta)
admin.site.register(Mantenimiento)
admin.site.register(DetalleMatenimiento)
admin.site.register(DetalleVenta)
admin.site.register(Cliente)
admin.site.register(Empleado)



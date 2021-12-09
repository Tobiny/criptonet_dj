from django.contrib import admin

# Register your models here.
from apps.app.models import *

admin.site.register(Producto)
admin.site.register(TipoProducto)
admin.site.register(Marca)
admin.site.register(Servicio)
admin.site.register(Mantenimiento)
admin.site.register(Client)
admin.site.register(Empleado)

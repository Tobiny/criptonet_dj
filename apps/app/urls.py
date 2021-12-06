from django.conf.urls import url
from django.urls import path, re_path
from apps.app import views
from apps.app.views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    #Productos
    url(r'^productos/$', views.VistasProductosListas.as_view(), name='productos'),
    url(r'^producto/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.ProductoDetalles.as_view(), name='producto_detalles'),
    url(r'^producto/crear/$', views.ProductosCrear.as_view(), name='productos_crear'),
    url(r'^producto/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$', views.ProductosUpdate.as_view(), name='productos_modificar'),
    url(r'^producto/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.ProductosBorrar.as_view(), name='productos_borrar'),
    #Tipos de productos
    url(r'^tipos/$', views.VistasTiposProductos.as_view(), name='tipos'),
    url(r'^tipo_producto/(?P<pk>[A-Za-z0-9]{3})/$', views.TipoDetalles.as_view(), name='tipo_detalles'),
    url(r'^tipo_producto/crear/$', views.TiposCrear.as_view(), name='tipos_crear'),
    url(r'^tipo_producto/(?P<pk>[A-Za-z0-9]{3})/modificar/$', views.TiposUpdate.as_view(), name='tipos_modificar'),
    url(r'^tipo_producto/(?P<pk>[A-Za-z0-9]{3})/borrar/$', views.TiposBorrar.as_view(), name='tipos_borrar'),
    #Marcas
    url(r'^marcas/$', views.VistasMarcas.as_view(), name='marcas'),
    url(r'^marca/(?P<pk>[A-Za-z0-9]{3})/$', views.MarcaDetalles.as_view(), name='marca_detalles'),
    url(r'^marca/crear/$', views.MarcasCrear.as_view(), name='marcas_crear'),
    url(r'^marca/(?P<pk>[A-Za-z0-9]{3})/modificar/$', views.MarcasUpdate.as_view(), name='marcas_modificar'),
    url(r'^marca/(?P<pk>[A-Za-z0-9]{3})/borrar/$', views.MarcasBorrar.as_view(), name='marcas_borrar'),
    #Empleados
    url(r'^empleados/$', views.VistasEmpleados.as_view(), name='empleados'),
    url(r'^empleado/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.EmpleadoDetalles.as_view(), name='empleado_detalles'),
    url(r'^empleado/crear/$', views.EmpleadosCrear.as_view(), name='empleados_crear'),
    url(r'^empleado/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$', views.EmpleadosUpdate.as_view(), name='empleados_modificar'),
    url(r'^empleado/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.EmpleadosBorrar.as_view(), name='empleados_borrar'),
    #Mantenimientos
    url(r'^mantenimientos/$', views.VistasMantenimientos.as_view(), name='mantenimientos'),
    url(r'^mantenimiento/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.MantenimientoDetalles.as_view(), name='mantenimiento_detalles'),
    url(r'^mantenimiento/crear/$', views.MantenimientosCrear.as_view(), name='mantenimientos_crear'),
    url(r'^mantenimiento/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$', views.MantenimientosUpdtate.as_view(), name='mantenimientos_modificar'),
    url(r'^mantenimiento/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.MantenimientosBorrar.as_view(), name='mantenimientos_borrar'),
    #Clientes
    url(r'^clientes/$', views.VistasClientes.as_view(), name='clientes'),
    url(r'^cliente/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.ClientesUpdate.as_view(), name='cliente_detalles'),
    url(r'^cliente/crear/$', views.ClientesCrear.as_view(), name='clientes_crear'),
    url(r'^cliente/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$', views.ClientesUpdate.as_view(), name='clientes_modificar'),
    url(r'^cliente/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.ClientesBorrar.as_view(), name='clientes_borrar'),
    #Ventas
    url(r'^ventas/$', views.VistasVentas.as_view(), name='ventas'),
    url(r'^venta/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.VentasDetalles.as_view(), name='venta_detalles'),
    url(r'^venta/crear/$', views.VentasCrear.as_view(), name='ventas_crear'),
    url(r'^venta/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$', views.VentasUpdate.as_view(), name='ventas_modificar'),
    url(r'^venta/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.VentasBorrar.as_view(), name='ventas_borrar'),
    #Servicos
    url(r'^servicios/$', views.VistasServicios.as_view(), name='servicios'),
    url(r'^servicio/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.ServiciosDetalles.as_view(), name='servicio_detalles'),
    url(r'^servicio/crear/$', views.ServiciosCrear.as_view(), name='servicios_crear'),
    url(r'^servicio/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$', views.ServiciosUpdate.as_view(), name='servicios_modificar'),
    url(r'^servicio/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.ServiciosBorrar.as_view(), name='servicios_borrar'),
    url(r'^servicio/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.ServiciosBorrar.as_view(), name='servicios_borrar'),

    path('exportar', views.export, name='export'),
    path('importar', views.importar, name='import'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]

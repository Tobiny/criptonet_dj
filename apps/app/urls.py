from django.conf.urls import url
from django.urls import path, re_path
from apps.app import views
from apps.app.views import *
from django.contrib import admin

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Productos
    url(r'^productos/$', views.VistasProductosListas.as_view(), name='productos'),
    url(r'^producto/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$',
        views.ProductoDetalles.as_view(), name='producto_detalles'),
    url(r'^producto/crear/$', views.ProductosCrear.as_view(), name='productos_crear'),
    url(r'^producto/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$',
        views.ProductosUpdate.as_view(), name='productos_modificar'),
    url(r'^producto/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$',
        views.ProductosBorrar.as_view(), name='productos_borrar'),
    # Tipos de productos
    url(r'^tipos/$', views.VistasTiposProductos.as_view(), name='tipos'),
    url(r'^tipo_producto/(?P<pk>[A-Za-z0-9]{3})/$', views.TipoDetalles.as_view(), name='tipo_detalles'),
    url(r'^tipo_producto/crear/$', views.TiposCrear.as_view(), name='tipos_crear'),
    url(r'^tipo_producto/(?P<pk>[A-Za-z0-9]{3})/modificar/$', views.TiposUpdate.as_view(), name='tipos_modificar'),
    url(r'^tipo_producto/(?P<pk>[A-Za-z0-9]{3})/borrar/$', views.TiposBorrar.as_view(), name='tipos_borrar'),
    # Marcas
    url(r'^marcas/$', views.VistasMarcas.as_view(), name='marcas'),
    url(r'^marca/(?P<pk>[A-Za-z0-9]{3})/$', views.MarcaDetalles.as_view(), name='marca_detalles'),
    url(r'^marca/crear/$', views.MarcasCrear.as_view(), name='marcas_crear'),
    url(r'^marca/(?P<pk>[A-Za-z0-9]{3})/modificar/$', views.MarcasUpdate.as_view(), name='marcas_modificar'),
    url(r'^marca/(?P<pk>[A-Za-z0-9]{3})/borrar/$', views.MarcasBorrar.as_view(), name='marcas_borrar'),
    # Empleados
    url(r'^empleados/$', views.VistasEmpleados.as_view(), name='empleados'),
    url(r'^empleado/(?P<pk>\d+)/$', views.EmpleadoDetalles.as_view(), name='empleado_detalles'),
    url(r'^empleado/crear/$', views.EmpleadosCrear.as_view(), name='empleados_crear'),
    url(r'^empleado/(?P<pk>\d+)/modificar/$', views.EmpleadosUpdate.as_view(), name='empleados_modificar'),
    url(r'^empleado/(?P<pk>\d+)/borrar/$', views.EmpleadosBorrar.as_view(), name='empleados_borrar'),
    # Mantenimientos
    url(r'^mantenimientos/$', views.VistasMantenimientos.as_view(), name='mantenimientos'),
    url(r'^mantenimientos/(?P<pk>\d+)/$', views.MantenimientosDetalles.as_view(), name='mantenimientos_detalles'),
    url(r'^mantenimientos/crear/$', views.MantenimientosCrear.as_view(), name='mantenimientos_crear'),
    url(r'^mantenimientos/(?P<pk>\d+)/modificar/$', views.MantenimientosUpdate.as_view(),
        name='mantenimientos_modificar'),
    url(r'^mantenimientos/(?P<pk>\d+)/borrar/$', views.MantenimientosBorrar.as_view(), name='mantenimientos_borrar'),
    # Clientes
    url(r'^clientes/$', views.VistasClientes.as_view(), name='clientes'),
    url(r'^cliente/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.ClienteDetalles.as_view(), name='cliente_detalles'),
    url(r'^cliente/crear/$', views.ClientesCrear.as_view(), name='clientes_crear'),
    url(r'^cliente/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$', views.ClientesUpdate.as_view(), name='clientes_modificar'),
    url(r'^cliente/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.ClientesBorrar.as_view(), name='clientes_borrar'),

    path('sales/', views.SaleView.as_view(), name='ventas'),
    path('sales/nueva_venta', views.SaleCreateView.as_view(), name='ventas-crear'),
    path('sales/<pk>/borrar', views.SaleDeleteView.as_view(), name='ventas-borrar'),
    path("sales/<billno>", views.SaleBillView.as_view(), name="recibo-venta"),

    path('compras/', views.ComprasView.as_view(), name='compras'),
    path('compras/nueva_compra', views.ComprasCreateView.as_view(), name='compras_crear'),
    path('compras/editar_compra/<billno>', views.ComprasModificarView.as_view(), name='compras_modificar'),
    path('compras/<pk>/borrar', views.ComprasBorrarView.as_view(), name='compras_borrar'),
    path("compras/<billno>", views.ReciboComprasView.as_view(), name="recibo_compra"),

    #Reportes
    path('reportes_prod', views.reportes_productos, name='rep_productos'),
    path('reportes_client', views.reportes_clientes, name='rep_clientes'),
    path('reportes_comp', views.reportes_compras, name='rep_compras'),
    path('reportes_vent', views.reportes_ventas, name='rep_ventas'),
    path('reportes', views.reportes_pivot, name='reportes'),
    path('data', views.reportes_datos, name='datos_reportes'),
    #Importar y exportar
    path('exportar', views.export, name='export'),
    path('importar', views.importar, name='import'),
    # Coincide con cualquier archivo html
    re_path(r'^.*\.*', views.pages, name='pages'),
    path('admin/', admin.site.urls, name='admin-site'),  # Ruta de admin Django
]

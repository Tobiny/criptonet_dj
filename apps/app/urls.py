from django.conf.urls import url
from django.urls import path, re_path
from apps.app import views
from apps.app.views import *

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

    # Clientes
    url(r'^clientes/$', views.VistasClientes.as_view(), name='clientes'),
    url(r'^cliente/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.ClienteDetalles.as_view(), name='cliente_detalles'),
    url(r'^cliente/crear/$', views.ClientesCrear.as_view(), name='clientes_crear'),
    url(r'^cliente/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$', views.ClientesUpdate.as_view(), name='clientes_modificar'),
    url(r'^cliente/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.ClientesBorrar.as_view(), name='clientes_borrar'),


    path('invoices',views.invoices, name='invoices'),
    # Create URL Paths
    path('invoices/create', views.createInvoice, name='create-invoice'),
    path('invoices/create-build/<slug:slug>', views.createBuildInvoice, name='create-build-invoice'),

    # Delete an invoice
    path('invoices/delete/<slug:slug>', views.deleteInvoice, name='delete-invoice'),

    # PDF and EMAIL Paths
    path('invoices/view-pdf/<slug:slug>', views.viewPDFInvoice, name='view-pdf-invoice'),
    path('invoices/view-document/<slug:slug>', views.viewDocumentInvoice, name='view-document-invoice'),


    path('exportar', views.export, name='export'),
    path('importar', views.importar, name='import'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]

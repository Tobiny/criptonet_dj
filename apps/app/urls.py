from django.conf.urls import url
from django.urls import path, re_path
from apps.app import views
from apps.app.views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    url(r'^productos/$', views.VistasProductosListas.as_view(), name='productos'),
    url(r'^producto/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/$', views.ProductoDetalles.as_view(), name='producto_detalles'),
    url(r'^productos/crear/$', views.ProductosCrear.as_view(), name='productos_crear'),
    url(r'^producto/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/modificar/$', views.ProductosUpdate.as_view(), name='productos_modificar'),
    url(r'^producto/(?P<pk>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})/borrar/$', views.ProductosBorrar.as_view(), name='productos_borrar'),

    path('empleados/', vistas_e, name='vistas_e'),
    path('servicios/', vistas_s, name='vistas_s'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

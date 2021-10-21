from django.urls import path, re_path
from apps.app import views
from apps.app.views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('productos/', vistas_p, name='vistas_p'),
    path('empleados/', vistas_e, name='vistas_e'),
    path('servicios/', vistas_s, name='vistas_s'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]

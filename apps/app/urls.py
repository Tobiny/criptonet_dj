"""locallibrary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

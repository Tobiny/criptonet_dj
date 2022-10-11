# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from core.wsgi import *
from django.test import TestCase
from apps.app.models import Client

# Create your tests here.
query = Client.objects.all()
t = Client.objects.get(uniqueId="43e459aa48ba402b907a191e4b5ffabc")
print(t.nombreCliente)

# select from Tabla
# query = Cliente.objects.all()
# print(query)

#insercion
#t.Type()
# t.name = 'Accionista"
# t.save()
# t.save()

# edicion

#t = Type.objects.get(pk-1)
#t.name = 'Accionsdk19283'
#t.save()
#eliminacion

# try:
#     c = Client.objects.get(uniqueId="43e459aa48ba402b907a191e4b5ffabc")
#     c.nombreCliente = "Cualquier Otro Nombre"
#     c.save()
# except Exception as e:
#     print(e)
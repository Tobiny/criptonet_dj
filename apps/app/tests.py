# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from datetime import date

from core.wsgi import *
from django.test import TestCase
from apps.app.models import Cliente, Producto, TipoProducto, Marca, Empleado, Mantenimientos
import csv

# Create your tests here.
#Abrir el csv con el encoding UTF-8 y lo pasa a una lista (debe estar en la carpeta testcases)
# with open('testcases/Testcases.csv', newline='', encoding="utf-8") as f:
#     data = list(csv.reader(f, delimiter=","))

#For por toda la lista, insertando los datos en el modelo Producto, si necesitas insertar en
#Otros modelos ve a apps/app/models, ahi vienen los que usamos.
#Sino sabes que modelo es me preguntas
# for d in data:
#     producto = Producto(modelo=d[0], descripcion=d[1], tipo_producto=TipoProducto.objects.get(id_tipo=d[2]),
#                         marca=Marca.objects.get(id_marca=d[3]))
#     producto.save()
#Cuando termines de usarlo, los comentas, no lo vayas a volver a correr, de lo contrario te va volver a insertar


#Abrir el csv con el encoding UTF-8 y lo pasa a una lista (debe estar en la carpeta testcases)
# with open('testcases/clientes.csv', newline='', encoding="utf-8") as f:
#     data = list(csv.reader(f, delimiter=","))
#
# #For por toda la lista, insertando los datos en el modelo Producto, si necesitas insertar en
# #Otros modelos ve a apps/app/models, ahi vienen los que usamos.
# #Sino sabes que modelo es me preguntas
# for d in data:
#     producto = Client(nombreCliente=d[0], domicilio=d[1], estado=d[2], codigoPostal=d[3], numTelefono=d[4], dirEmail=d[5], rfcCliente=d[6])
#     producto.save()
#Cuando termines de usarlo, los comentas, no lo vayas a volver a correr, de lo contrario te va volver a insertar

#Abrir el csv con el encoding UTF-8 y
#Abrir el csv con el encoding UTF-8 y


#For por toda la lista, insertando los datos en el modelo Producto, si necesitas insertar en
#Otros modelos ve a apps/app/models, ahi vienen los que usamos.
#Sino sabes que modelo es me preguntas
#Cuando termines de usarlo, los comentas, no lo vayas a volver a correr, de lo contrario te va volver a insertar







# Ignora esto, esto es de guía para hacer otras cosas
# #select from Tabla
# query = Cliente.objects.all()
# print(query)

# #insercion
# t.Type()
# t.name = 'Accionista"
# t.save()
# t.save()

# #edicion
#
# t = Type.objects.get(pk-1)
# t.name = 'Accionsdk19283'
# t.save()
# #eliminacion

# try:
#     c = Client.objects.get(uniqueId="43e459aa48ba402b907a191e4b5ffabc")
#     c.nombreCliente = "Cualquier Otro Nombre"
#     c.save()
# except Exception as e:
#     print(e)


# query = Client.objects.all()
# t = Client.objects.get(uniqueId="43e459aa48ba402b907a191e4b5ffabc")
# print(t.nombreCliente)


print('Antonio'=='ANTONIO')
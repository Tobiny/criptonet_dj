from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import FloatField

# Create your models here.
class Producto(models.Model):
    id_producto = models.CharField(max_length=14, primary_key=True)
    nom = models.CharField(max_length=25)
    precio_venta = FloatField(max_length=25)
    existencia = models.IntegerField()

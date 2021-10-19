from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import FloatField, DecimalField


# Create your models here.
class Producto(models.Model):
    id_producto = models.CharField(max_length=14, primary_key=True)
    nom = models.CharField(max_length=25)
    precio_venta = DecimalField(max_length=25, decimal_places=2, max_digits=16)
    existencia = models.IntegerField()

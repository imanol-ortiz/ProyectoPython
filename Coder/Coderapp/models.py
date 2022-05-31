from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=20)
    stock=models.IntegerField()
    #precio=models.FloatField()
    #disponibilidad=models.BooleanField()

class Vendedor(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    telefono=models.IntegerField()
    #email=models.EmailField()

class Sucursal(models.Model):
    numero=models.IntegerField()
    direccion=models.CharField(max_length=40)
    #email=models.EmailField


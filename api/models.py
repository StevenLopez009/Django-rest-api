from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=50) 
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()

class Factura(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()

class Categorias(models.Model):
    descripcion = models.CharField(max_length=200)

class Productos(models.Model): 
    nomProducto = models.CharField(max_length=50)
    desProducto = models.CharField(max_length=200) 
    catProducto = models.CharField(max_length=20) 
    canProducto = models.PositiveIntegerField(default=True) 
    precioProducto = models.PositiveBigIntegerField(default=True)
    estProducto = models.BooleanField(default=True)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, null=True, blank=True)

class Ventas(models.Model):
    cantidad = models.CharField(max_length=20) 
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Productos)


from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()

class Proveedores(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.BigIntegerField()

class Productos(models.Model):
    nomProducto = models.CharField(max_length=50)
    desProducto = models.CharField(max_length=200)
    catProducto = models.CharField(max_length=20)
    canProducto = models.PositiveIntegerField(default=0)
    precioProducto = models.PositiveIntegerField(default=0)  # Cambiado a default=0
    estProducto = models.BooleanField(default=True)
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE, null=True, blank=True)

class Factura(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Productos)
    precio_total = models.PositiveIntegerField(default=0)  # Nuevo campo

@receiver(m2m_changed, sender=Factura.productos.through)
def actualizar_precio_total(sender, instance, **kwargs):
    if kwargs['action'] in ['post_add', 'post_remove', 'post_clear']:
        instance.precio_total = sum(producto.precioProducto for producto in instance.productos.all())
        instance.save()

class Categorias(models.Model):
    descripcion = models.CharField(max_length=200)

class Ventas(models.Model):
    cantidad = models.CharField(max_length=20)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Productos)


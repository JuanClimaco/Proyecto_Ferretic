from django.db import models

class Ferretic(models.Model):
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)


class Proveedor(models.Model):
    Ferretic = models.ForeignKey(Ferretic, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=20)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    precio_publico= models.IntegerField()
    cantidad_stock = models.IntegerField()

class Pedido(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    proveedor = models.ForeignKey( Proveedor, on_delete=models.PROTECT)
    fecha_pedido = models.DateTimeField(auto_now=False)
    cantidad_pedido = models.IntegerField()
    precio_proveedor = models.IntegerField()

class Empleado(models.Model):
    nombres_apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    fecha_nacimiento = models.DateTimeField()
    nombre_usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)


class Cliente(models.Model):
     nombre = models.CharField(max_length=50)
     identificacion= models.CharField(max_length=50)
     telefono= models.CharField(max_length=50)
     correo = models.CharField(max_length=50)

class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    punto_venta = models.CharField(max_length=50)
    fecha_venta = models.DateTimeField(auto_now=True)
    cantidad_venta=models.IntegerField()
    total_factura = models.IntegerField()
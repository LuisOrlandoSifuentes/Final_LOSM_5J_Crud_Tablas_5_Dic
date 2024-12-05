from django.db import models

# Create your models here.

class Sucursal(models.Model):
    id_sucursal = models.PositiveIntegerField(primary_key=True)
    nombre_sucursal = models.CharField(max_length=255)
    numero_empleado = models.PositiveIntegerField()
    calle_sucursal = models.CharField(max_length=255)
    productos = models.CharField(max_length=255)
    num_producto = models.PositiveIntegerField()
    telefono = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre_sucursal
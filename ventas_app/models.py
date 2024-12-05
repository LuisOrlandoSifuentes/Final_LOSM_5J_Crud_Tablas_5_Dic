from django.db import models

# Create your models here.
class Venta(models.Model):
    id_ventas = models.PositiveIntegerField(primary_key=True)
    id_empleado = models.PositiveIntegerField()
    id_cliente = models.PositiveIntegerField()
    id_producto = models.PositiveIntegerField()
    fecha_venta = models.DateField(null=False,blank=False)
    cantidad = models.PositiveIntegerField()
    id_sucursal = models.PositiveIntegerField()
    total = models.PositiveIntegerField()

    def __str__(self):
        return self.id_ventas
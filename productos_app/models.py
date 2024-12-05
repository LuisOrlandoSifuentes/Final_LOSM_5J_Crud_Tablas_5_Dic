from django.db import models

# Create your models here.
class Producto(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    stock=models.PositiveIntegerField()
    id_sucursal=models.PositiveIntegerField()
    id_provedor=models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
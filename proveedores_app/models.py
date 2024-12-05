from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    telefono = models.PositiveIntegerField()
    producto = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    nie = models.CharField(max_length=50)
    suc_asignadas = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
from django.db import models

# Create your models here.
class Empleado(models.Model):
    id_empleado = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    fecha_nac = models.DateField(null=False,blank=False)
    sexo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=255)
    telefono = models.PositiveIntegerField()
    curp = models.CharField(max_length=18)
    id_sucursal=models.PositiveIntegerField()

    def __str__(self):
        return self.nombre
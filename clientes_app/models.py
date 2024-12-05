from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.PositiveIntegerField(primary_key=True)
    direccion = models.CharField(max_length=255)
    nombre = models.CharField(max_length=100)
    telefono = models.PositiveIntegerField()
    tipo_de_pago = models.CharField(max_length=50)
    fecha_nac = models.DateField(null=False,blank=False)
    productos_adquiridos = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
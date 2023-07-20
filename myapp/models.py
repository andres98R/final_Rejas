from django.db import models


# Create your models here.
class Pais(models.Model):
    idpais = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    poblacion = models.IntegerField()
    estado = models.BooleanField(default=True)

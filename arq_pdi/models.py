from django.db import models


class Caso(models.Model):
    tipo_caso = models.CharField(max_length=50, unique=False)
    ubicacion = models.CharField(max_length=100)
    fono = models.IntegerField()
    desc_caso = models.TextField()

# Create your models here.

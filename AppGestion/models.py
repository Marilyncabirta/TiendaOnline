from django.db import models

# Create your models here.

class Producto(models.Model):
    id=models.PositiveSmallIntegerField(primary_key=True)
    nombre=models.CharField(max_length=30,blank=False)
    imagen1=models.CharField(max_length=254,blank=True)
    precio=models.FloatField()
    def __str__(self):
        return self.nombre 
from django.db import models

# Create your models here.
class Region(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad=models.CharField(max_length=50)

class Candidato(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField(max_length=2)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
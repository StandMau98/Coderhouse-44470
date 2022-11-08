from django.db import models

# Create your models here.


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()
pass


class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.IntegerField()
    nacimiento = models.DateField()


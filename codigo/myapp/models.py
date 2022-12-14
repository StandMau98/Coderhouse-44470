from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Torneo(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} -> Categoria: {self.categoria} "

class Palas(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
      return f"{self.nombre} --> ARS {self.precio} --> Stock: {self.stock} "


class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
      return f"{self.nombre}  {self.apellido} --> Email {self.email} "
    
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.IntegerField()

    def __str__(self):
      return f"{self.nombre}  {self.apellido} --> Email {self.email} --> Telefono {self.telefono} "


class Avatar(models.Model):
  user=models.ForeignKey(User, on_delete=models.CASCADE)
  imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
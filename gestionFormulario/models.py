from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.


class Personas(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Cedula = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=130)
    Colegio_Electoral = models.CharField(max_length=50)
    CentroDeVotacion = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=13)
    Telefono = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Edad = models.IntegerField()
    Sector = models.CharField(max_length=50)

    def __str__(self):

        return self.Nombre + "   " + (self.Apellido) +  "  || " +  "Cedula:  " + (self.Cedula)

from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class Ubicacion(models.Model):
    nom_comisaria = models.CharField(max_length=200)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    nombredd = models.CharField(max_length=50)
    nombrepp = models.CharField(max_length=50)
    nombredi = models.CharField(max_length=50)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_comisaria


class UbicacionForm(ModelForm):
    class Meta:
        model = Ubicacion
        fields = "__all__"


class UbicacionComisaria(models.Model):
    INEI = models.CharField(max_length=200, null=True, blank=True)
    CPNP = models.CharField(max_length=200, null=True, blank=True)
    NOMBREDD = models.CharField(max_length=200, null=True, blank=True)
    NOMBREPP = models.CharField(max_length=200, null=True, blank=True)
    NOMBREDI = models.CharField(max_length=200, null=True, blank=True)
    GPS = models.CharField(max_length=200, null=True, blank=True)
    MACREGPOL = models.CharField(max_length=200, null=True, blank=True)
    REGPOL = models.CharField(max_length=200, null=True, blank=True)
    DIVPOL = models.CharField(max_length=200, null=True, blank=True)
    COMISARIA = models.CharField(max_length=200, null=True, blank=True)
    TIPO = models.CharField(max_length=200, null=True, blank=True)


class Denuncia(models.Model):
    DNI = models.CharField(max_length=8, blank=True, null=True)
    NOMBRE = models.CharField(max_length=200, blank=True, null=True)
    APELLIDO = models.CharField(max_length=200, blank=True, null=True)
    COMISARIA = models.CharField(max_length=200)
    FECHA = models.DateField()
    DESCRIPCION = models.TextField()
# Create your models here.


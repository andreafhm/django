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
	user = models.ForeignKey('auth.User',on_delete=models.CASCADE)

	def __str__(self):
		return self.nom_comisaria

class UbicacionForm(ModelForm):
	class Meta:
		model = Ubicacion
		fields = "__all__"



# Create your models here.

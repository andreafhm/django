from django.contrib import admin
from .models import Ubicacion,Denuncia

# Register your models here.
# Registramos el nuevo modelo creado
class DenunciaAdmin(admin.ModelAdmin):
    list_display = ['DNI','NOMBRE','APELLIDO']

admin.site.register(Ubicacion)
admin.site.register(Denuncia,DenunciaAdmin)

from django.contrib import admin
from .models import Ubicacion,UbicacionComisaria,Denuncia

# Register your models here.
# Registramos el nuevo modelo creado

class UbiacionC(admin.ModelAdmin):
      list_display = ['COMISARIA']
class DenunciaAdmin(admin.ModelAdmin):
      list_display = ['DNI','NOMBRE','APELLIDO','DELITO','COMISARIA']
admin.site.register(Ubicacion)
admin.site.register(UbicacionComisaria,UbiacionC)
admin.site.register(Denuncia,DenunciaAdmin)

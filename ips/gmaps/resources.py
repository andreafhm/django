from import_export import resources
from .models import UbicacionComisaria


class PersonaResource(resources.ModelResource):
    class Meta:
        model = UbicacionComisaria

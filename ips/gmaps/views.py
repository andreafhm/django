from django.shortcuts import render
from tablib import Dataset
from .resources import PersonaResource
from .models import UbicacionComisaria, Denuncia
from .forms import DenunciaForm
from django.http import HttpRequest


def index(request):
    return render(request, 'index.html')


def comisaria(request):
    ubicaciones = UbicacionComisaria.objects.all()
    context = {
        'ubs': ubicaciones,
        'titulo': "Mapa",
    }
    return render(request, 'comisaria.html', context)


def estadistica(request):
    denuncias = Denuncia.objects.all()
    context = {
        'titulo': "Estadisticas",
        'denuncias': denuncias
    }
    return render(request, 'estadistica.html', context)

def denunciaEstadistica(request):
    denunciaEstadistica = Denuncia.objects.all()
    data = {
        'estadistica':denunciaEstadistica
    }
    return render(request,'DenunciaEstadistica.html',data)

#def denunciar(request):
#    denuncia = DenunciaForm()
#    return render(request, 'Denuncias.html', {"form": denuncia})


def denunciar(request):
    data = {
        'form':DenunciaForm()
    }
    denuncia = DenunciaForm(request.POST)
    if denuncia.is_valid():
        denuncia.save()
    return render(request,'Denuncias.html',data)


#def procesar_denuncia(request):
#    denuncia = DenunciaForm(request.POST)
#    if denuncia.is_valid():
#        denuncia.save()
#    return render(request, 'Denuncias.html', {"form": denuncia, "mensaje": "ok"})


def importar(request):
    if request.method == 'POST':
        persona_resource = PersonaResource()
        dataset = Dataset()
        # print(dataset)
        nuevas_personas = request.FILES['xlsfile']
        # print(nuevas_personas)
        imported_data = dataset.load(nuevas_personas.read())
        # print(dataset)
        result = persona_resource.import_data(dataset, dry_run=True, raise_errors=True)  # Test the data import
        print(result.has_errors())
        if not result.has_errors():
            persona_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'importar.html')

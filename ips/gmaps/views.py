from django.shortcuts import render
from tablib import Dataset

from .resources import PersonaResource


def index(request):
    return render(request, 'index.html')


def comisaria(request):
    return render(request, 'comisaria.html')


def denuncia(request):
    return render(request, 'home.html')


def estadistica(request):
    return render(request, 'home.html')


def importar(request):
    if request.method == 'POST':
        persona_resource = PersonaResource()
        dataset = Dataset()
        # print(dataset)
        nuevas_personas = request.FILES['xlsfile']
        print(nuevas_personas)
        imported_data = dataset.load(nuevas_personas.read())
        print(dataset)
        result = persona_resource.import_data(dataset, dry_run=True)  # Test the data import
        # print(result.has_errors())
        if not result.has_errors():
            persona_resource.import_data(dataset, dry_run=False)  # Actually import now
    return render(request, 'importar.html')

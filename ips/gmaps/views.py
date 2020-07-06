from django.shortcuts import render
from django.shortcuts import render_to_response

def index(request):
    return render(request,'index.html')

def comisaria(request):
    return render(request, 'comisaria.html')

def denuncia(request):
    return render(request,'home.html')

def estadistica(request):
    return render(request,'home.html')
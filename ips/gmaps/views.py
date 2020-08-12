from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from tablib import Dataset
from django.contrib.auth.forms import UserCreationForm
from .forms import DenunciaForm
from .models import UbicacionComisaria, Denuncia
from .prueba import UnauthorizedError
from .resources import PersonaResource


def index(request):
    try:
        verficiarLogin(request)
        return render(request, 'index.html')
    except UnauthorizedError:
        return login(request)


def verficiarLogin(request):
    if not request.user.is_authenticated:
        raise UnauthorizedError()


def comisaria(request):
    try:
        verficiarLogin(request)
        ubicaciones = UbicacionComisaria.objects.all()
        context = {
            'ubs': ubicaciones,
            'titulo': "Mapa",
        }
        return render(request, 'comisaria.html', context)
    except   UnauthorizedError:
        return unauthorized(request)


def estadistica(request):
    try:
        verficiarLogin(request)
        denuncias = Denuncia.objects.all()
        context = {
            'titulo': "Estadisticas",
            'denuncias': denuncias
        }
        return render(request, 'estadistica.html', context)
    except UnauthorizedError:
        return unauthorized(request)


def denunciaEstadistica(request):
    try:
        verficiarLogin(request)
        denunciaEstadistica = Denuncia.objects.all()
        data = {
            'estadistica': denunciaEstadistica
        }
        return render(request, 'DenunciaEstadistica.html', data)
    except UnauthorizedError:
        return unauthorized(request)


# def denunciar(request):
#    denuncia = DenunciaForm()
#    return render(request, 'Denuncias.html', {"form": denuncia})


def denunciar(request):
    try:
        verficiarLogin(request)
        data = {
            'form': DenunciaForm(),
            'ubicaciones': UbicacionComisaria.objects.all()
        }
        denuncia = DenunciaForm(request.POST)
        if denuncia.is_valid():
            denuncia.save()
        return render(request, 'Denuncias.html', data)
    except UnauthorizedError:
        return unauthorized(request)


# def procesar_denuncia(request):
#    denuncia = DenunciaForm(request.POST)
#    if denuncia.is_valid():
#        denuncia.save()
#    return render(request, 'Denuncias.html', {"form": denuncia, "mensaje": "ok"})


def importar(request):
    try:
        verficiarLogin(request)
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
    except UnauthorizedError:
        return unauthorized(request)


def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form': form})


def login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/login')


def unauthorized(request):
    return render(request, "unauthorized.html")

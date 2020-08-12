from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comisaria/', views.comisaria, name="comisaria"),
    path('test/', views.importar, name="test"),
    path('importar/', views.importar, name="importar"),
    path('denunciar/', views.denunciar, name="denunciar"),
    path('estadistica/', views.estadistica, name="estadistica"),
    # path('guardarDenuncia/', views.procesar_denuncia, name="guardarDenuncia"),
    path('estadisticaD/', views.denunciaEstadistica, name="estadisticaDenuncia"),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('unauthorized', views.unauthorized),

]

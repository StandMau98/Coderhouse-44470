from django.urls import path
from myapp.views import *



urlpatterns = [
    path('', inicio, name='c-inicio'),
    path('palas/', palas, name='c-palas'),
    path('profesores/', profesores, name='c-profesores'),
    path('profesores/crear/', creacion_profesores, name='coder-profesores-crear'),
    path('torneo/', torneo, name='c-torneo'),
    path('torneo/crear/', creacion_torneo, name='coder-torneo-crear'),
    path('torneo/buscar/', buscar_torneo, name='coder-torneo-buscar'),
    path('torneo/buscar/resultados/', resultados_busqueda_torneo, name='coder-torneo-buscar-resultados'),
    path('contacto/', contacto, name='c-contacto')

    
]
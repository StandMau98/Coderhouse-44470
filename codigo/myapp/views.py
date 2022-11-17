from django.shortcuts import render
from django.http import HttpResponse
#from datetime import datetime
from django.template import  Template, Context

from myapp.models import Torneo, Profesor
from myapp.form import ProfesorFormulario



# Create your views here.



def inicio(request):
    return render(request, 'myapp/index.html')

    
def torneo(request):
    return render(request, 'myapp/torneo.html')

def creacion_torneo(request):
    if request.method == "POST":
        nombre_torneo = request.POST['torneo']
        numero_categoria = int(request.POST['categoria'])

        torneo = Torneo(nombre=nombre_torneo, categoria=numero_categoria)
        torneo.save()
    return render(request, 'myapp/torneo_formulario.html')

def buscar_torneo(request):
    return render(request, 'myapp/busqueda_torneo.html')

def resultados_busqueda_torneo(request):
    nombre_torneo = request.GET['nombre_curso']
    #iconteins es una forma de buscar sus cadenas de cada una de las registros
    torneo = Torneo.objects.filter(nombre__icontains=nombre_torneo)
    return render(request, 'myapp/resultados_busquedas_torneo.html', {'torneo': torneo})
    
def palas(request):
    return render(request, 'myapp/palas.html')
    
def profesores(request):
    return render(request, 'myapp/profesores.html')

def creacion_profesores(request):
    if request.method == 'POST':
        formulario = ProfesorFormulario(request.POST)

        #Validamos que le formulario no tenga problemas
        if formulario.is_valid():
            #recuperamos los datos del atributo cleaned_data
            data = formulario.cleaned_data

            profesor = Profesor(nombre = data['nombre'], apellido = data['apellido'], email = data['email'])
            profesor.save()
        
        
    
    formulario = ProfesorFormulario(request.POST)
    contexto = {'formulario': formulario}
    return render(request, 'myapp/profesores_form.html', contexto)
    
def contacto(request):
    return render(request, 'myapp/contacto.html')



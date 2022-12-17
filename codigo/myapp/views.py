from django.shortcuts import render, redirect
from django.http import HttpResponse
#from datetime import datetime
from django.template import  Template, Context

from myapp.models import Torneo, Profesor, Palas, Avatar
from myapp.form import ProfesorFormulario, TorneoForm, RegisterForm, UserEditForm, AvatarForm, Contacto
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin # para las clases
from django.contrib.auth.decorators import login_required # para las funciones

# Create your views here.



def inicio(request):
    if request.user.is_authenticated:
        img= Avatar.objects.filter(user=request.user.id).order_by('-id')[0]
        imagen_url= img.imagen.url
    else:
        imagen_url= ''
    return render(request, 'myapp/index.html', {'imagen_url': imagen_url})

@login_required    
def torneo(request):
    

    errores = ""

    # Validamos tipo depeticion
    if request.method == "POST":
        #cargamos los datos en el formulario
        formulario = TorneoForm(request.POST)
     #     validamos los datos
        if formulario.is_valid():
            #recuperamos los datos snitizados
            data = formulario.cleaned_data
            #creamos el torneo
            torneo = Torneo(nombre=data['nombre'], categoria = data['categoria'])
            #guardamos el torneo
            torneo.save()
        else:
            #si el formulario no es valido guardamos los errores para mostrarlos
            errores = formulario.errors

#Recuperar todos los torneo de la BD
    torneo = Torneo.objects.all()
#Cremaos le form vacio
    formulario = TorneoForm()
#Creamos el contexto
    contexto = {"listado_torneo": torneo, "formulario": formulario, "errores": errores}
#Retornamos la respuesta
    return render(request, 'myapp/torneo.html', contexto)


def buscar_torneo(request):
    return render(request, 'myapp/busqueda_torneo.html')

def resultados_busqueda_torneo(request):
    nombre_torneo = request.GET['nombre_torneo']
    #iconteins es una forma de buscar sus cadenas de cada una de las registros
    torneo = Torneo.objects.filter(nombre__icontains=nombre_torneo)
    return render(request, 'myapp/resultados_busquedas_torneo.html', {'torneo': torneo})

def delete_torneo(request, id):
    torneo = Torneo.objects.get(id=id)
    torneo.delete()
    return redirect('c-torneo')

def update_torneo(request, id):
    torneo= Torneo.objects.get(id=id)
    if request.method == "POST":
        formulario = TorneoForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            torneo.nombre=data['nombre']
            torneo.categoria = data ['categoria']
            torneo.save()
            return redirect('c-torneo')
        else:
            return render(request, 'coder/edit_torneo.html', {'formulario': formulario, "errores": formulario.errors})
    else:
        formulario = TorneoForm(initial={'nombre': torneo.nombre, 'categoria':torneo.categoria})
        return render(request, 'myapp/edit_torneo.html', {'formulario': formulario, "errores": ""})


    
def palas(request):
    return render(request, 'myapp/palas.html')

def listPalas(request):
    if request.user.is_authenticated:
        img= Palas.objects.filter(palas=request.palas.id).order_by('-id')[0]
        foto_url= img.foto.url
    else:
        foto_url= ''
    return render(request, 'myapp/palas.html',  {'foto_url': foto_url})
    
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

def verMensajes(request):
    
    return render(request, 'myapp/verMensajes.html')


class PalasList(LoginRequiredMixin, ListView):
    model = Palas
    template_name = 'myapp/list_palas.html'

class Palasdetail(DetailView):
    model = Palas
    template_name = 'myapp/detail_palas.html'

class PalasCreate(CreateView):
    model = Palas
    success_url = '/coder/palas/'
    fields = ['nombre', 'precio', 'stock', 'foto']

class PalasUpdate(UpdateView):
    model = Palas
    success_url = '/coder/palas/'
    fields = ['nombre', 'precio', 'stock', 'foto']

class PalasDelete(DeleteView):
    model = Palas
    success_url = '/coder/palas/'


def loguin_sesion(request):
    errors = ''
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username = data['username'], password=data['password'])

            if user is not None :
                login(request, user)
                return redirect('c-inicio')
            else:
                return render(request, 'myapp/login.html', {'form': formulario, 'errors': 'Credenciales invalidas'} )
        else:
            return render(request, 'myapp/login.html', {'form': formulario, 'errors': formulario.errors} )
        

    formulario = AuthenticationForm()
    return render(request, "myapp/login.html",{'form': formulario, 'errors': errors} )


def register_user(request):
    if request.method == 'POST':
        formulario = RegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            return redirect('c-inicio')
        else:
            return render(request, 'myapp/register.html', {'form': formulario, 'errors': formulario.errors} )


    formulario = RegisterForm()
    return render(request, 'myapp/register.html', {'form': formulario} )


@login_required
def edit_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        # *cargar informacion en el form
        formulario = UserEditForm(request.POST)

        # ! validacion del form
        if formulario.is_valid():
             data = formulario.cleaned_data

        # * actualizacion dleusuario con los datos del form
             usuario.email = data['email']
             usuario.first_name = data['first_name']
             usuario.last_name = data['last_name']

             usuario.save()
             return redirect('c-inicio')
        else:
            return render(request,'myapp/edit_perfil.html',{'form': formulario, 'errors': formulario.errors} )
        
    else:
        #* crear form vacio
        formulario = UserEditForm(initial={'email': usuario.email, 'first_name': usuario.first_name, 'last_name': usuario.last_name} )
        pass
    return render (request, 'myapp/edit_perfil.html', {'form': formulario})


@login_required
def agregar_avatar(request):
    if request.method=='POST':
        formulario= AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():
            data= formulario.cleaned_data
            usuario = request.user
            avatar = Avatar(user=usuario, imagen=data['imagen'])
            avatar.save()
            return redirect('c-inicio')
        else:
            return render(request, 'myapp/agregar_avatar.html', {'form': formulario, 'errors': formulario.errors})
    
    formulario= AvatarForm()

    return render(request,'myapp/agregar_avatar.html', {'form': formulario})
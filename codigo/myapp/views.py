from django.shortcuts import render
from django.http import HttpResponse
#from datetime import datetime
from django.template import  Template, Context
from myapp.models import Familia

# Create your views here.


def familiares(request):
    archivo= open(r'C:\Users\Sebastian\Desktop\practicasPython\codigo\nuevoproject\templates\bd_Familiares_desafio.html')
    plantilla = Template(archivo.read())
    archivo.close()
    fam = Familia.objects.all()
    
    fam_lista = {'listaFam': fam}


    contexto = Context(fam_lista)
    documento = plantilla.render(contexto)


    return HttpResponse(documento)



    #plantilla = loader.get_template('bd_Familiares_desafio.html')
    #documento = plantilla.render (fam)
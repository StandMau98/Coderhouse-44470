from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader



def vista_saludo(request):
    return HttpResponse("""
    hola codersss""")


def anio_nacimiento(request,edad):

    edad= int(edad)

    anio_nac = datetime.now().year - edad

    return HttpResponse(f'naciste en{anio_nac} ')



def vista_plantilla(request):
    archivo= open(r'C:\Users\Sebastian\Desktop\practicasPython\codigo\nuevoproject\templates\plantilla_bonita.html')

    plantilla= Template(archivo.read())

    archivo.close()

    datos = {"nombre": "Leonel",'fecha': datetime.now(), 'apellido': 'Gareis'}

    contexto = Context(datos)

    documento = plantilla.render(contexto)
    
    return HttpResponse(documento)


def vista_listado_alumnos(request):
    archivo = open(r"C:\Users\Sebastian\Desktop\practicasPython\codigo\nuevoproject\templates\listado_alumnos.html")

    plantilla = Template(archivo.read())

    archivo.close()

    listado_alumnos = ['Sebastian Pastor', 'Maximiliano Pastor', 'Santiago Ortiz', 'Agustin russo', 'Barbara Vivante', 'Leonel Gareis']

    datos = {"tecnologia":"python", "listado_alumnos": listado_alumnos}

    contexto = Context(datos)

    documento = plantilla.render (contexto)

    return HttpResponse(documento)



def vista_listado_alumnos2(request):
    listado_alumnos = ['Sebastian Pastor', 'Maximiliano Pastor', 'Santiago Ortiz', 'Agustin russo', 'Barbara Vivante', 'Leonel Gareis']

    datos = {"tecnologia":"python", "listado_alumnos": listado_alumnos}

    plantilla = loader.get_template('listado_alumnos.html')
    documento = plantilla.render(datos)

    return HttpResponse(documento)


    
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pais
from django.contrib import messages

from .models import Editorial

# Create your views here.
def index(request):
    return render(request, "index.html", {"titulo": "Inicio"})


# PAIS -----------------------------


def listar_paises(request):
    paises = Pais.objects.all()
    return render(request, "paises.html", {"paises": paises, "titulo": "Paises"})


# en el archivo views.py


def registrar_pais(request):
    if request.method == "POST":
        codigo = request.POST["codigo"]
        nombre = request.POST["nombre"]
        poblacion = request.POST["poblacion"]

        # Manejar el valor del campo "estado" como un campo booleano
        estado = request.POST.get("estado", False) == "on"

        # Crear el nuevo país en la base de datos
        nuevo_pais = Pais(
            codigo=codigo, nombre=nombre, poblacion=poblacion, estado=estado
        )
        nuevo_pais.save()
        messages.success(request, "Pais registrado correctamente")
        return redirect("listar_paises")

    return render(request, "registrar_pais.html", {"titulo": "Registrar país"})


def eliminar_pais(request, id):
    pais = Pais.objects.get(pk=id)
    pais.delete()
    messages.success(request, "Pais eliminado correctamente")
    return redirect("listar_paises")

# en el archivo views.py

def registrar_editorial(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        url = request.POST['url']
        estado = request.POST.get('estado', False)
        imagen = request.POST['imagen']
        nueva_editorial = Editorial(nombre=nombre, url=url, imagen=imagen, estado=estado)
        nueva_editorial.save()

        return redirect('listar_editorial')

    return render(request, 'registrar_editorial.html', {'titulo': 'Registrar Editorial'})



# EDITORIAL -----------------------------


def listar_editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, "editoriales.html", {"editoriales": editoriales, "titulo": "Editoriales"})


def registrar_editorial(request):
    return render(
        request, "registrar_editorial.html", {"titulo": "Registrar editorial"}
    )


def listar_editorial(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editorial.html', {'editoriales': editoriales})

def eliminar_editorial(request, id):
    editorial = Editorial.objects.get(pk=id)
    editorial.delete()
    messages.success(request, "Editorial eliminado correctamente")
    return redirect("listar_editoriales")

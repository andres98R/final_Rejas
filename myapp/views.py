from django.shortcuts import render, redirect, get_object_or_404
from .models import Pais
from django.contrib import messages


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


# EDITORIAL -----------------------------


def listar_editoriales(request):
    return render(request, "editoriales.html", {"titulo": "Editoriales"})


def registrar_editorial(request):
    return render(
        request, "registrar_editorial.html", {"titulo": "Registrar editorial"}
    )

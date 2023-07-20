from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {
        'titulo':'Inicio'
    })

# PAIS -----------------------------

def listar_paises(request):
    return render(request, 'paises.html', {
        'titulo':'Paises'
    })

def registrar_pais(request):
    return render(request, 'registrar_pais.html', {
        'titulo':'Registrar país'
    })

# EDITORIAL -----------------------------

def listar_editoriales(request):
    return render(request, 'editoriales.html', {
        'titulo':'Editoriales'
    })

def registrar_editorial(request):
    return render(request, 'registrar_editorial.html', {
        'titulo':'Registrar editorial'
    })
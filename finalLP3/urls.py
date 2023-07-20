"""finalLP3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="inicio"),
    path("index/", views.index, name="inicio"),
    path("paises/", views.listar_paises, name="listar_paises"),
    path("editoriales/", views.listar_editoriales, name="listar_editoriales"),
    path("registrar_pais/", views.registrar_pais, name="registrar_pais"),
    path("registrar_editorial/", views.registrar_editorial, name="registrar_editorial"),
    path("eliminar_pais/<int:id>", views.eliminar_pais, name="eliminar_pais"),
    path("eliminar_editorial/<int:id>", views.eliminar_editorial, name="eliminar_editorial"),
]

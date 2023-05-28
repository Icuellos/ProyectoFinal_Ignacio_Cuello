"""
URL configuration for ProyectoCuello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from MyAPP.views import index, about, Crear_form, contacto, crear_articulo, crear_nuevo, Crear_Equipo, Crear_Liga, Crear_Proyecto, CrearNuevaLiga, CrearNuevoEquipo, CrearNuevoFormulario, CrearNuevoProyecto, lista_articulos, Proyectos, buscar_equipos, buscar, BuscarEquipoForm, BuscarFormulario, detalle_equipo, detalle_liga, Equipo, eliminar_liga, eliminar_equipo, Equipos
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MyAPP.urls')),
    path('Perfiles/', include('Perfiles.urls')),
     path('admin', admin.site.urls),
    path('', index),
    path('index/', index, name='index'),
    path('articulos/', lista_articulos, name='lista_articulos'),
    path('about/', about, name='about'),
    path('contacto/', contacto, name='contacto'),
    path('Proyectos/', Proyectos, name='Proyectos'),
    path('Crear_form/', Crear_form, name='form'),
    path('Crear_Proyecto/', Crear_Proyecto, name='Crear_Proyecto'),
    path('Crear_Liga/', Crear_Liga, name='Crear_Liga'),
    path('buscar_equipos/',buscar_equipos, name='buscar_equipos'),
    path('Equipo/', Equipo, name='Equipo'),
    path('Crear_Equipo/', Crear_Equipo, name='Crear_Equipo'),
    path('equipo/<int:equipo_id>/', detalle_equipo, name='detalle_equipo'),
    path('eliminar_liga/<int:liga_id>/', eliminar_liga, name='eliminar_liga'),
    path('eliminar_liga/<int:liga_id>/', eliminar_liga, name='eliminar_liga'),
    path('eliminar_equipo/<int:equipo_id>/', eliminar_equipo, name='eliminar_equipo'),
    path('liga/<int:liga_id>/', detalle_liga, name='detalle_liga'),
    path('buscar/', buscar, name='buscar'),
    path('crear_articulo/', crear_articulo, name='crear_articulo'),
    
]

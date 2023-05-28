
from django.http import HttpResponse, JsonResponse
from .models import Proyecto, Equipos, Liga, Articulo
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CrearNuevoFormulario, CrearNuevoProyecto, CrearNuevaLiga, CrearNuevoEquipo, BuscarEquipoForm, BuscarFormulario, ArticuloForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    title = "Misión" 
    return render(request, "Index.html", 
                  {'title': title})

def about(request):
    username = "icuello"
    return render(request, "About.html", {'username': username})

def Crear_form(request):
   # Proyectos = list(Proyecto.objects.values())
   #Equipos = equipos.objects.all()
   return render(request, 'Crear_form.html',
                 {'form': CrearNuevoFormulario})
   
def Proyectos(request):
   # Proyectos = list(Proyecto.objects.values())
   articulos = Articulo.objects.all()
   return render(request, 'Proyectos.html', {'articulos': articulos})  
   
def Crear_Proyecto(request):
    if request.method == 'GET':
     return render(request, 'Crear_Proyecto.html', 
                  {'form': CrearNuevoProyecto()})
    else:
        print (request.POST)
        Proyectos = Proyecto.objects.create(name=request.POST["name"])
        return render(request, 'Crear_Proyecto.html', 
                  {'form': CrearNuevoProyecto()
    })
        
def Crear_Liga(request):
    if request.method == 'POST':
        form = CrearNuevaLiga(request.POST)
        if form.is_valid():
            liga = Liga()  
            liga.name = form.cleaned_data['name']  #
            liga.save()  

            return redirect('Proyectos')  
    else:
        form = CrearNuevaLiga()  

    return render(request, 'Crear_Liga.html', {'form': form})

#def Equipo(request):
    #equipos = Equipos.objects.all()
    #return render(request, 'Equipo.html', {'equipos': equipos}) 
def Crear_Equipo(request):
    ligas = Liga.objects.all()

    if request.method == 'POST':
        form = CrearNuevoEquipo(request.POST)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.liga = form.cleaned_data['liga']
            equipo.save()
            return redirect('Equipo')
    else:
        form = CrearNuevoEquipo()

    return render(request, 'crear_equipo.html', {'form': form, 'ligas': ligas})

#def Crear_Equipo(request):
    if request.method == 'POST':
         form = CrearNuevoEquipo(request.POST)
         if form.is_valid():
            name = form.cleaned_data['name']
            liga = form.cleaned_data['liga']
            equipo = Equipos(name=name, liga=liga)
            #equipo = Equipos(name=name) comentamos esto para ver si podemos guardar equpo en ligas
            equipo.save()
            return redirect('Equipo')   
    else: 
        form = CrearNuevoEquipo()

    return render(request, 'Crear_Equipo.html', {'form': form})

def Equipo(request):
    equipos = Equipos.objects.all()
    return render(request, 'Equipo.html', {'equipos': equipos})    
 

def buscar_equipos(request):
    query = request.GET.get('query')
    equipos = None

    if query is not None:
        equipos = Equipos.objects.filter(name__icontains=query)

    return render(request, 'buscar_equipos.html', {'equipos': equipos, 'query': query})

def detalle_equipo(request, equipo_id):
    equipo = Equipos.objects.get(id=equipo_id)
    return render(request, 'detalle_equipo.html', {'equipo': equipo})  
  
#def detalle_equipo(request, equipo_id):
#    equipo = get_object_or_404(Equipos, id=equipo_id)
#    return render(request, 'detalle_equipo.html', {'equipo': equipo})    

#PARA ELIMINAR EQUIPOS
def eliminar_liga(request, liga_id):
    liga = Liga.objects.get(id=liga_id)
    liga.delete()
    return redirect('Proyectos')

#PARA ELIMINAR UNA LIGA
def eliminar_equipo(request, equipo_id):
    equipo = Equipos.objects.get(id=equipo_id)
    equipo.delete()
    return redirect('Equipo')

#Para crear una vista de los detalles de la liga
def detalle_liga(request, liga_id):
    liga = get_object_or_404(Liga, id=liga_id)
    equipos = liga.equipos.all()
    return render(request, 'detalle_liga.html', {'liga': liga, 'equipos': equipos})

def buscar(request):
    form = BuscarFormulario()

    if request.method == 'POST':
        form = BuscarFormulario(request.POST)
        if form.is_valid():
            termino = form.cleaned_data['termino']
            tipo_busqueda = form.cleaned_data['tipo_busqueda']

            if tipo_busqueda == 'equipo':
                equipos = Equipos.objects.filter(name__icontains=termino)
                return render(request, 'buscar.html', {'form': form, 'equipos': equipos, 'tipo_busqueda': tipo_busqueda, 'termino': termino})
            elif tipo_busqueda == 'liga':
                ligas = Liga.objects.filter(name__icontains=termino)
                return render(request, 'buscar.html', {'form': form, 'ligas': ligas, 'tipo_busqueda': tipo_busqueda, 'termino': termino})

    return render(request, 'buscar.html', {'form': form})


def crear_nuevo(request):
    if request.method == 'POST':
        formulario = CrearNuevoFormulario(request.POST)
        if formulario.is_valid():
            # Guardar el formulario y redireccionar
            formulario.save()
            return redirect('index')
    else:
        formulario = CrearNuevoFormulario()
    return render(request, 'crear_nuevo.html', {'formulario': formulario})

#COMENZANDO CON LOS ARTICULOS
def crear_articulo(request):
    if request.method == 'POST':
        formulario = ArticuloForm(request.POST, request.FILES)
        if formulario.is_valid():
            # Asignar el autor actual al campo 'autor'
            articulo = formulario.save(commit=False)
            articulo.autor = request.user
            
            # Obtener el proyecto al que se desea asociar el artículo
            proyecto = Proyecto.objects.get(id=1)  # Reemplaza 1 con el ID del proyecto deseado
            
            articulo.proyecto = proyecto
            articulo.save()
            return redirect('Proyectos')
    else:
        formulario = ArticuloForm()
    
    contexto = {'formulario': formulario}
    return render(request, 'crear_articulo.html', contexto)



def contacto(request):
    mensaje_enviado = False

    if request.method == 'POST':
        # Procesar el formulario y guardar los datos
        mensaje_enviado = True

    context = {
        'mensaje_enviado': mensaje_enviado
    }

    return render(request, 'contacto.html', context)
                  
def lista_articulos(request):
    articulos = Articulo.objects.all()
    contexto = {'articulos': articulos}
    return render(request, 'lista_articulos.html', contexto)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Proyecto(models.Model):
    name = models.CharField(max_length=200)
    # Para retornar los nombres de los proyectos
    def __str__(self):
         return self.name

class Equipos(models.Model):    
    name = models.CharField(max_length=200)

    def __str__(self):
         return self.name
    

class Liga(models.Model):    
     name = models.CharField(max_length=200)
     #proyecto =models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
     def __str__(self):
         return self.name     
     

class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    juguete = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo     
    

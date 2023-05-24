from django.db import models

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
    
class Puntuacion(models.Model):    
     Puntos = models.CharField(max_length=200)
     proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
        
     def __str__(self):
         return self.Puntos
     
class Goleadores(models.Model):    
     Nombre = models.CharField(max_length=200)
     proyecto =models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
     def __str__(self):
         return self.Nombre  
     
class Estadios(models.Model):    
     Nombre = models.CharField(max_length=200)
     proyecto =models.ForeignKey(Proyecto, on_delete=models.CASCADE)  
     
     def __str__(self):
         return self.Nombre      
     
# Eliminar desde aqui en caso de error
class Liga(models.Model):    
     name = models.CharField(max_length=200)
     #proyecto =models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    
     def __str__(self):
         return self.name     
    

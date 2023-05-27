from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega los campos adicionales que deseas incluir en el perfil
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.user.username
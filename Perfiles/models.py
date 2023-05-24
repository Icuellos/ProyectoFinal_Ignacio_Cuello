from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega aquí tus campos adicionales de perfil
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
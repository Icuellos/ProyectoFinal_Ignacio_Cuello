from django.contrib import admin
from .models import Proyecto, Equipos, Liga, Articulo

# Register your models here.
admin.site.register(Proyecto)
admin.site.register(Equipos)
admin.site.register(Liga)
admin.site.register(Articulo)
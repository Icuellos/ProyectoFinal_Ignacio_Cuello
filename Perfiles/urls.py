from django.urls import path
from . import views


app_name = 'Perfiles'

urlpatterns = [
    # ... otras rutas de tu proyecto ...
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]

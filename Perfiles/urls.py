from django.urls import include, path
from . import views

app_name = 'Perfiles'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio-sesion'),
    path('cerrar-sesion/', views.cerrar_sesion, name='cerrar-sesion'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]



from django.urls import include, path
from . import views
from .views import inicio_sesion

app_name = 'Perfiles'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]



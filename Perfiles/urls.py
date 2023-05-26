from django.urls import path
from . import views
from .views import perfil_create

app_name = 'Perfiles'

urlpatterns = [
    # ... otras rutas de tu proyecto ...
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('perfiles/', views.perfil_list, name='perfil_list'),
    path('perfiles/<int:perfil_id>/', views.perfil_detail, name='perfil_detail'),
    path('create/', views.perfil_create, name='perfil_create'),
    path('perfiles/update/<int:perfil_id>/', views.perfil_update, name='perfil_update'),
    path('perfiles/delete/<int:perfil_id>/', views.perfil_delete, name='perfil_delete'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registro/', views.registro, name='registro'),
    # ... otras rutas de tu proyecto ...
]



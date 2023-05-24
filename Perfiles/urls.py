from django.urls import path, include
from perfiles.views import RegistroUsuarioView, LoginUsuarioView, LogoutUsuarioView

app_name = 'perfiles'

urlpatterns = [
    # ... otras rutas de tu proyecto ...
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('login/', LoginUsuarioView.as_view(), name='login'),
    path('logout/', LogoutUsuarioView.as_view(), name='logout'),
]

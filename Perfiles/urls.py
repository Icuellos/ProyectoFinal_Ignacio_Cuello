from django.urls import path, include
from .import views
from django.contrib.auth import login, logout
from .forms import RegisterForm
from perfiles.views import LoginUsuarioView

app_name = 'perfiles'

urlpatterns = [
    # ... otras rutas de tu proyecto ...
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    path('login/', LoginUsuarioView.as_view(), name='login'),
]

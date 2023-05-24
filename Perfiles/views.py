from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm

class RegistroUsuarioView(CreateView):
    form_class = RegistroForm
    template_name = 'registro.html'
    success_url = reverse_lazy('perfiles:login')

class LoginUsuarioView(LoginView):
    template_name = 'login.html'
    authentication_form = LoginForm

class LogoutUsuarioView(LogoutView):
    next_page = reverse_lazy('perfiles:login')



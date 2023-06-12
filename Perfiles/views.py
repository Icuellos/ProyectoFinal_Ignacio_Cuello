
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .forms import RegistroForm
from django.contrib.auth.models import User

def registro(request):
    error_message = None  # Variable para almacenar el mensaje de error

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)
            return redirect('index')  # Redirigir a una página de registro exitoso
        else:
            error_message = 'Las contraseñas no coinciden.'
    else:
        form = RegistroForm()
    
    context = {'form': form, 'error_message': error_message}  # Pasar el mensaje de error a la plantilla
    return render(request, 'registro.html', context)

def inicio_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error_message = "Nombre de usuario o contraseña incorrectos."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('index')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo."
    else:
        error_message = ""

    context = {'error_message': error_message}
    return render(request, 'login.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')








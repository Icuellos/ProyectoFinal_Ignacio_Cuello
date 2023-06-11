
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserCreationForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

def registro(request):
    error_message = ""
    password_mismatch = False

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1 != password2:
                error_message = "Las contraseñas no coinciden. Por favor, inténtalo nuevamente."
            else:
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index')
        else:
            return render(request, 'registro.html', {'form': form})
    else:
        form = UserCreationForm()
    
    return render(request, 'registro.html', {'form': form, 'error_message': error_message, 'password_mismatch': password_mismatch})

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








from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Perfil
from .forms import PerfilForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render, redirect



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('index')  # Cambia 'index' por la URL a la que deseas redirigir después del inicio de sesión exitoso
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('index')  # Cambia 'index' por la URL a la que deseas redirigir después del cierre de sesión


def perfil_list(request):
    perfiles = Perfil.objects.all()
    return render(request, 'perfil_list.html', {'perfiles': perfiles})


def perfil_detail(request, perfil_id):
    perfil = get_object_or_404(Perfil, pk=perfil_id)
    return render(request, 'perfil_detail.html', {'perfil': perfil})

def perfil_create(request):
    if request.method == 'POST':
        form = PerfilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio
    else:
        form = PerfilForm()
    
    context = {'form': form}
    return render(request, 'perfil_create.html', context)





def perfil_update(request, perfil_id):
    perfil = get_object_or_404(Perfil, pk=perfil_id)
    if request.method == 'POST':
        form = PerfilForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil_list')
    else:
        form = PerfilForm(instance=perfil)
    return render(request, 'perfil_update.html', {'form': form, 'perfil': perfil})


def perfil_delete(request, perfil_id):
    perfil = get_object_or_404(Perfil, pk=perfil_id)
    if request.method == 'POST':
        perfil.delete()
        return redirect('perfil_list')
    return render(request, 'perfil_delete.html', {'perfil': perfil})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


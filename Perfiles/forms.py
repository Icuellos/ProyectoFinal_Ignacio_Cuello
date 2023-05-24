from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroForm(UserCreationForm):
    fecha_nacimiento = forms.DateField()
    telefono = forms.CharField(max_length=20)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'fecha_nacimiento', 'telefono']

class LoginForm(AuthenticationForm):
    # Puedes personalizar los campos del formulario de inicio de sesión si lo deseas
    pass
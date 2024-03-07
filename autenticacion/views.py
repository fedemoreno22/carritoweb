from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.

class Registro(View):
    def get(self, request):
        form = CustomUserCreationForm() # Creación del formulario
        return render(request, "registro/registro.html", {"form":form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST) # Almacenar los datos introducidos en el form
        if form.is_valid():
            usuario = form.save() # Guardar en la base de datos, tabla auth_user
            login(request, usuario) # auto login después de registrarse
            return redirect('Home')
        else:
            for msg in form.error_messages: # para que muestre los msjs de error
                messages.error(request, form.error_messages[msg])
            
            return render(request, "registro/registro.html", {"form":form})
        
def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            nombre_usuario =form.cleaned_data.get("username")
            contrasegna = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contrasegna)

            if usuario is not None:
                login(request, usuario)
                return redirect("Home")
            else:
                messages.error(request, "Usuario no válido")
        else:
            messages.error(request, "Información incorrecta")
            
    form = AuthenticationForm()
    return render(request, "login/login.html",{"form":form})
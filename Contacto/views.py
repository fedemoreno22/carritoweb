from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)

        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("Mensaje desde App Django",
                                 f"El usuario {nombre} con la dirección {email} escribe lo siguiente:\n\n{contenido}",
                                 "", ["loreliz.dev@gmail.com"], reply_to=[email])
            
            try:
                email.send()
                return redirect("/contacto/?valid") # Redirige a la url indicada
            except:
                return redirect("/contacto/?novalid")

    return render(request,"contacto/contacto.html", {'formulario':formulario_contacto})
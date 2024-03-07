from .carrito import Carrito # para que funcione la primera vez, despues borrar y *

# Este archivo se utiliza para crear una variable global
# Luego, se registra la ruta en settings-templates

def importe_total_carro(request):
    carrito = Carrito(request) # *
    total = 0
    if request.user.is_authenticated:
        for key, value in request.session["carrito"].items():
            total += float(value["precio"])
    else:
        total = "Debes hacer login"

    return {"importe_total_carro":total}
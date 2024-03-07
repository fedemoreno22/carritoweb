from django.shortcuts import redirect
from .carrito import Carrito
from Tienda.models import Producto

# Create your views here.

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto=producto)
    return redirect("Tienda")

def vaciar_carro(request):
    carrito = Carrito(request)
    carrito.vaciar_carro()
    return redirect("Tienda")
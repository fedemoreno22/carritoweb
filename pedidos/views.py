from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from carrito.carrito import Carrito
from pedidos.models import LineaPedido, Pedido

# Create your views here.

@login_required(login_url="/autenticacion/login")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carrito = Carrito(request)
    lineas_pedido = list()

    for key, value in carrito.carrito.items():
        lineas_pedido.append(LineaPedido(
            producto_id = key,
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido) # Insertar en la base de datos multiples objetos de una sola vez

    enviar_mail(
        pedido=pedido,
        lineas_pedido = lineas_pedido,
        nombre_usuario = request.user.username,
        email_usuario = request.user.email
        )
    
    return redirect('pedido_procesado', pedido_id=pedido.id)

def pedido_procesado(request, pedido_id):
    carrito = Carrito(request)
    pedido = Pedido.objects.get(id=pedido_id)
    lineas_pedido = pedido.lineapedido_set.all()
    nombre_usuario = request.user.username
    email_usuario = request.user.email
    importe_total_producto = []
    importe_total_pedido = 0

    for linea in lineas_pedido:
        importe_total_linea = (linea.cantidad * linea.producto.precio)
        importe_total_producto.append(importe_total_linea)
        importe_total_pedido += importe_total_linea

    # Combinar 2 listas
    datos_lineas = zip(lineas_pedido, importe_total_producto)

    carrito.vaciar_carro()

    messages.success(request, "Gracias por tu compra. El pedido se ha creado correctamente.")

    return render(request, "pedidos/pedido.html", {'pedido':pedido, 'datos_lineas':datos_lineas, 'nombre_usuario': nombre_usuario, 'email_usuario': email_usuario, 'importe_total_producto':importe_total_producto, 'importe_total_pedido':importe_total_pedido})

def enviar_mail(**kwargs):
    asunto = "Gracias por el pedido"
    mensaje = render_to_string("emails/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombre_usuario":kwargs.get("nombre_usuario"),
        "email_usuario":kwargs.get("email_usuario")
    })

    mensaje_texto = strip_tags(mensaje) # Para ignorar etiquetas html
    from_email = "loreliz.dev@gmail.com"
    to = kwargs.get("email_usuario")

    send_mail(asunto, mensaje_texto, from_email,[to],html_message=mensaje)
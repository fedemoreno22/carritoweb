from django.urls import path
from . import views

urlpatterns = [
    path('', views.procesar_pedido, name="procesar_pedido"),
    path('pedido/<int:pedido_id>', views.pedido_procesado, name="pedido_procesado"),
]
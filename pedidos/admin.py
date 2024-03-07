from django.contrib import admin
from .models import Pedido, LineaPedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):
    readonly_fields = ('created')

admin.site.register([Pedido, LineaPedido])
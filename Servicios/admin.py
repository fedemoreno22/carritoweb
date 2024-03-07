from django.contrib import admin
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin): # Para que estos campos aparezcan en el panel de admin
    readonly_fields = ('created', 'updated') # Para que sean solo de lectura

admin.site.register(Servicio, ServicioAdmin)
from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='servicios') # para que las imagenes que se suban se guarden en una carpeta específica
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta: # Para especificar características a la clase
        verbose_name = 'servicio' # Para especificar el nombre que se quiere que tenga el modelo dentro de la tabla
        verbose_name_plural = 'servicios'

    def __str__(self):
        return self.titulo
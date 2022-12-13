from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = RichTextUploadingField(verbose_name='Contenido')
    image = models.ImageField(upload_to='services', verbose_name="Imagen")
    pricing = models.IntegerField(verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-updated']

    def __str__(self):
        return self.title

class Pedido(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    direccion = models.CharField(max_length=200, verbose_name='Calle y numero')
    colonia = models.CharField(max_length=200, verbose_name='Colonia o fraccionamiento')  
    total = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total')
    correo = models.EmailField(verbose_name='Email')
    fecha = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')

    class Meta:
        verbose_name= 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-fecha']
    
    def __str__(self):
        return str(self.id)

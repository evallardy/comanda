from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
from django.db.models import F
from django.db.models import Case, When, Value, CharField

from core.models import ACTIVO_PRODUCTO, TIPO_PRODUCTO, TIPO, SINO, TIPO_SOLICITUD

class Grupo(models.Model, PermissionRequiredMixin):
    nombre = models.CharField("Nombre", max_length=255)
    estatus = models.IntegerField("Estatus", choices=ACTIVO_PRODUCTO, default=1)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['nombre']
        unique_together = ['nombre']
        db_table = 'Grupo'

    def __str__(self):
        return '%s' % (self.nombre)

class Insumo(models.Model, PermissionRequiredMixin):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name="insumo_grupo")
    nombre = models.CharField("Nombre", max_length=255)
    estatus = models.IntegerField("Estatus", choices=ACTIVO_PRODUCTO, default=1)
    imagen = models.IntegerField("Imagen insumo.", null=True, blank=True)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'
        ordering = ['grupo', 'nombre']
        unique_together = ['grupo', 'nombre']
        db_table = 'Insumo'

    def __str__(self):
        return f"{self.grupo.nombre} - {self.nombre}"

class Producto(models.Model, PermissionRequiredMixin):
    nombre = models.CharField("Nombre", max_length=255)
    breve = models.CharField("Breve descripción", max_length=255, null=True, blank=True)
    tipo = models.IntegerField("Tipo", choices=TIPO_PRODUCTO, default=1)
    insumos = models.JSONField("Ingredientes", null=True, blank=True)
    precio = models.DecimalField("Precio", max_digits=10, decimal_places=2, default=0)
    imagen = models.IntegerField("Imagen prod.", null=True, blank=True)
    estatus = models.IntegerField("Estatus", choices=ACTIVO_PRODUCTO, default=1)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['tipo','nombre',]
        unique_together = ['nombre']
        db_table = 'Producto'

    def __str__(self):
        return ' %s, %s, $ %s' % (dict(TIPO_PRODUCTO).get(self.tipo), self.nombre, self.precio)

class Paquete(models.Model, PermissionRequiredMixin):
    nombre = models.CharField("Promoción", max_length=255)
    descripcion = models.CharField("Descripción", max_length=255, null=True, blank=True)
    tipo = models.IntegerField("Tipo", choices=TIPO, default=1)
    componentes = models.JSONField("Componentes", null=True, blank=True)
    precio = models.DecimalField("Precio", max_digits=10, decimal_places=2, default=0)
    imagen = models.IntegerField("Imagen paq.", null=True, blank=True)
    estatus = models.IntegerField("Estatus", choices=ACTIVO_PRODUCTO, default=1)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Paquete'
        verbose_name_plural = 'Paquetes'
        ordering = ['tipo', 'nombre',]
        db_table = 'Paquete'

    def __str__(self):
        return ' %s, $ %s, %s' % (self.nombre, self.precio, dict(ACTIVO_PRODUCTO).get(self.estatus))

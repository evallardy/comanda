from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models

from core.models import ACTIVO_PRODUCTO, TIPO_PRODUCTO

class Producto(models.Model, PermissionRequiredMixin):
    nombre = models.CharField("Nombre", max_length=255)
    tipo = models.IntegerField("Tipo", choices=TIPO_PRODUCTO, default=1)
    ingredientes = models.JSONField("Ingredientes", null=True, blank=True)
    precio = models.DecimalField("Precio", max_digits=10, decimal_places=2, default=0)
    estatus = models.IntegerField("Estatus", choices=ACTIVO_PRODUCTO, default=1)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['tipo','nombre',]
        db_table = 'Producto'

    def __str__(self):
        return ' %s, %s, $ %s' % (dict(TIPO_PRODUCTO).get(self.tipo), self.nombre, self.precio)

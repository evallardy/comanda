from django.db import models

from core.models import *
from pedido.models import *


class Sorteo(models.Model, PermissionRequiredMixin):
    numero = models.IntegerField("Númnero sorteado", default=0)
    leido = models.IntegerField("Leído", choices=SINO, default=0)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Número'
        verbose_name_plural = 'Números'
        ordering = ['id']
        db_table = 'Sorteo'

    def __str__(self):
        return ' %s %s' % (self.numero, dict(SINO).get(self.leido))

class Cliente(models.Model, PermissionRequiredMixin):
    nombre = models.CharField("Nombre", max_length=255)
    estatus = models.IntegerField("Estatus", choices=ACTIVO_CLIENTE, default=1)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['nombre',]
        unique_together = ['nombre']
        db_table = 'Cliente'

    def __str__(self):
        return ' %s %s' % (self.nombre, dict(ACTIVO_CLIENTE).get(self.estatus))

class Cliente_comanda(models.Model, PermissionRequiredMixin):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="clienteCliente")
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, related_name="comandaCliente")
    cantidad = models.IntegerField("Tablas cliente", default=0)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Cliente comanda'
        verbose_name_plural = 'Cliente comandas'
        ordering = ['cliente_id', 'comanda_id']
        db_table = 'ClienteComanda'

    def __str__(self):
        return ' %s %s %s' % (self.cliente, self.comanda, self.cantidad)

class Tabla_bingo(models.Model, PermissionRequiredMixin):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="clienteTabla", blank=True, null=True)
    tabla_numero = models.IntegerField('Número de tabla', default=0)
    num1 = models.IntegerField('Número 1', default=0)
    sal1 = models.IntegerField('Salió 1', choices=SINO, default=0)
    num2 = models.IntegerField('Número 2', default=0)
    sal2 = models.IntegerField('Salió 2', choices=SINO, default=0)
    num3 = models.IntegerField('Número 3', default=0)
    sal3 = models.IntegerField('Salió 3', choices=SINO, default=0)
    num4 = models.IntegerField('Número 4', default=0)
    sal4 = models.IntegerField('Salió 4', choices=SINO, default=0)
    num5 = models.IntegerField('Número 5', default=0)
    sal5 = models.IntegerField('Salió 5', choices=SINO, default=0)
    num6 = models.IntegerField('Número 6', default=0)
    sal6 = models.IntegerField('Salió 6', choices=SINO, default=0)
    num7 = models.IntegerField('Número 7', default=0)
    sal7 = models.IntegerField('Salió 7', choices=SINO, default=0)
    num8 = models.IntegerField('Número 8', default=0)
    sal8 = models.IntegerField('Salió 8', choices=SINO, default=0)
    num9 = models.IntegerField('Número 9', default=0)
    sal9 = models.IntegerField('Salió 9', choices=SINO, default=0)
    num10 = models.IntegerField('Número 10', default=0)
    sal10 = models.IntegerField('Salió 10', choices=SINO, default=0)
    num11 = models.IntegerField('Número 11', default=0)
    sal11 = models.IntegerField('Salió 11', choices=SINO, default=0)
    num12 = models.IntegerField('Número 12', default=0)
    sal12 = models.IntegerField('Salió 12', choices=SINO, default=0)
    num13 = models.IntegerField('Número 13', default=0)
    sal13 = models.IntegerField('Salió 13', choices=SINO, default=0)
    num14 = models.IntegerField('Número 14', default=0)
    sal14 = models.IntegerField('Salió 14', choices=SINO, default=0)
    num15 = models.IntegerField('Número 15', default=0)
    sal15 = models.IntegerField('Salió 15', choices=SINO, default=0)
    num16 = models.IntegerField('Número 16', default=0)
    sal16 = models.IntegerField('Salió 16', choices=SINO, default=0)
    num17 = models.IntegerField('Número 17', default=0)
    sal17 = models.IntegerField('Salió 17', choices=SINO, default=0)
    num18 = models.IntegerField('Número 18', default=0)
    sal18 = models.IntegerField('Salió 18', choices=SINO, default=0)
    num19 = models.IntegerField('Número 19', default=0)
    sal19 = models.IntegerField('Salió 19', choices=SINO, default=0)
    num20 = models.IntegerField('Número 20', default=0)
    sal20 = models.IntegerField('Salió 20', choices=SINO, default=0)
    num21 = models.IntegerField('Número 21', default=0)
    sal21 = models.IntegerField('Salió 21', choices=SINO, default=0)
    num22 = models.IntegerField('Número 22', default=0)
    sal22 = models.IntegerField('Salió 22', choices=SINO, default=0)
    num23 = models.IntegerField('Número 23', default=0)
    sal23 = models.IntegerField('Salió 23', choices=SINO, default=0)
    num24 = models.IntegerField('Número 24', default=0)
    sal24 = models.IntegerField('Salió 24', choices=SINO, default=0)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Tabla'
        verbose_name_plural = 'Tablas'
        ordering = ['id']
        db_table = 'Tabla_bingo'

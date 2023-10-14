from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
from django.utils import timezone

from core.models import ACTIVA_COMANDA, ACTIVO_DETALLE, ACTIVO_PROMOCION, ACTIVO_CAJA
from producto.models import Producto
from usuario.models import Usuario
from core.models import Contable

def default_fecha_contable():
    contable = Contable.objects.filter(estatus=1).first()
    return contable.fecha if contable else timezone.now().date()

class Comanda(models.Model):
    mesa = models.CharField("Mesa", max_length=255, null=True, blank=True)
    observacion = models.CharField("Observación", max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioComanda", null=True, blank=True)
    usuario_cierra = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioComandaCierre", null=True, blank=True)
    usuario_cancela = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioComandaCancela", null=True, blank=True)
    usuario_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioComandaCliente", null=True, blank=True)
    estatus = models.IntegerField("Estatus", choices=ACTIVA_COMANDA, default=1)
    fecha_contable = models.DateField("Fecha Contable", default=default_fecha_contable)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Comanda'
        verbose_name_plural = 'Comandas'
        ordering = ['-fecha_alta',]
        unique_together = ['mesa', 'fecha_contable']
        db_table = 'Comanda'

    def __str__(self):
        return ' %s, %s, %s' % (self.mesa, self.observacion, dict(ACTIVA_COMANDA).get(self.estatus))


class Caja(models.Model, PermissionRequiredMixin):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, verbose_name="Comanda")
    descripcion = models.CharField("Tipo", max_length=255)
    especifico = models.CharField("Descripción", max_length=255, null=True, blank=True)
    cantidad = models.IntegerField("Cantidad", default=1)
    precio_unitario = models.DecimalField("Precio unitario", max_digits=10, decimal_places=2, default=0)
    importe = models.DecimalField("Importe", max_digits=10, decimal_places=2, default=0)
    estatus = models.IntegerField("Estatus", choices=ACTIVO_CAJA, default=1)
    usuario_elabora = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioCajaElabora", null=True, blank=True)
    usuario_cobra = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioCajaCobra", null=True, blank=True)
    usuario_cancela = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioCajaCancela", null=True, blank=True)
    descripcion_cancela = models.CharField("Descripción", max_length=255, null=True, blank=True)
    fecha_contable = models.DateField("Fecha Contable", default=default_fecha_contable)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Operación'
        verbose_name_plural = 'Operaciones'
        ordering = ['comanda','-fecha_alta',]
        db_table = 'Caja'

    def __str__(self):
        return ' %s, %s, %s, %s' % (self.comanda, self.descripcion, self.importe, dict(ACTIVO_DETALLE).get(self.estatus))


class Detalle(models.Model, PermissionRequiredMixin):
    caja = models.ForeignKey(Caja, on_delete=models.CASCADE, verbose_name="Caja")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    nom_paquete = models.CharField("Paquete", max_length=255, null=True, blank=True)
    nom_producto = models.CharField("Producto", max_length=255, null=True, blank=True)
    especifico = models.CharField("Especificación", max_length=255, null=True, blank=True)
    nota = models.CharField("Observación", max_length=255)
    especificacion = models.JSONField("Detalle", null=True, blank=True)
    cantidad = models.IntegerField("Cantidad", default=1)
    precio_unitario = models.DecimalField("Precio unitario", max_digits=10, decimal_places=2, default=0)
    importe = models.DecimalField("Importe", max_digits=10, decimal_places=2, default=0)
    estatus = models.IntegerField("Estatus", choices=ACTIVO_DETALLE, default=1)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioDetalle", null=True, blank=True)
    usuario_elabora = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioDetalleElabora", null=True, blank=True)
    usuario_entrega = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioDetalleEntrega", null=True, blank=True)
    usuario_cobra = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioDetalleCobra", null=True, blank=True)
    usuario_cancela = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioDetalleCancela", null=True, blank=True)
    usuario_reasigna = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioDetalleReasigna", null=True, blank=True)
    fecha_contable = models.DateField("Fecha Contable", default=default_fecha_contable)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'
        ordering = ['caja','-fecha_alta',]
        db_table = 'Detalle'

    def __str__(self):
        return ' %s, %s, %s, %s' % (self.caja, self.nom_producto, self.importe, dict(ACTIVO_DETALLE).get(self.estatus))

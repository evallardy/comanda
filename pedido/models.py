from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models
from django.utils import timezone

from core.models import ACTIVA_COMANDA, ACTIVO_DETALLE
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
        db_table = 'Comanda'

class Detalle(models.Model, PermissionRequiredMixin):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE, verbose_name="Comanda")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    nom_producto = models.CharField("Nombre", max_length=255, null=True, blank=True)
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
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'
        ordering = ['comanda','-fecha_alta',]
        db_table = 'Detalle'

    def crear_copia(self):
        for _ in range(self.cantidad - 1):
            copia = Detalle.objects.create(
                comanda=self.comanda,
                producto=self.producto,
                nom_producto=self.nom_producto,
                nota=self.nota,
                especificacion=self.especificacion,
                cantidad=1,
                precio_unitario=self.precio_unitario,
                importe=self.importe,
                estatus=self.estatus,
                usuario=self.usuario,
                usuario_elabora=self.usuario_elabora,
                usuario_entrega=self.usuario_entrega,
                usuario_cobra=self.usuario_cobra,
                usuario_cancela=self.usuario_cancela,
                usuario_reasigna=self.usuario_reasigna,
                fecha_modificacion=self.fecha_modificacion,
                fecha_alta=self.fecha_alta
            )

        self.cantidad = 1
        self.save()
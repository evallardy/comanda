from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models

from usuario.models import Usuario

ACTIVA_COMANDA = (
    (0, 'Cancelado'),
    (1, 'Actva'),
    (2, 'Pre-pagada'),
    (3, 'Cerrada'),
)
ACTIVO_DETALLE = (
    (0, 'Cancelado'),
    (1, 'Solicitado'),
    (2, 'Elaborado'),
    (3, 'Entregado'),
    (4, 'Pagado'),
    (5, 'Cancelado elaborado'),
    (6, 'Cancelado difinitivo'),
)
ACTIVO_PRODUCTO = (
    (0, 'Baja'),
    (1, 'Activo'),
)
ESTATUS_CONTABLE = (
    (0, 'Cerrado'),
    (1, 'Abierto'),
)
TIPO_PRODUCTO = (
    (0, 'S/T'),
    (1, 'Cocina'),
    (2, 'Bar'),
)

class Contable(models.Model, PermissionRequiredMixin):
    fecha = models.DateField("Fecha de operación")
    observacion = models.CharField("Observación", max_length=255, null=True, blank=True)
    usuario_abre = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioContaleAbre", null=True, blank=True)
    usuario_cierra = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="UsuarioContableCierra", null=True, blank=True)
    estatus = models.IntegerField("Estatus", choices=ESTATUS_CONTABLE, default=1)
    fecha_modificacion = models.DateTimeField("Fecha modificación", auto_now=True)
    fecha_alta = models.DateTimeField("Fecha alta", auto_now_add=True)

    class Meta:
        verbose_name = 'Fecha de operación'
        verbose_name_plural = 'Fechas de operación'
        ordering = ['-fecha',]
        db_table = 'FechaOperacion'
        permissions = (
            ('cocina', 'Cocina consulta'),
            ('cocina_termina', 'Cocina termina'),
            ('cocina_cancela', 'Cocina cancela'),

            ('bar', 'Bar consulta'),
            ('bar_termina', 'Bar termina'),
            ('bar_cancela', 'Bar cancela'),

            ('servicio', 'Comandas consulta'),
            ('servicio_nueva', 'Comanda nueva'),
            ('servicio_solicitar', 'Comanda solicita'),
            ('servicio_cancelar', 'Comanda cancela'),
            ('servicio_pagar', 'Comanda paga'),
            ('servicio_ver', 'Comanda detalle'),
            ('servicio_cierra', 'Comanda cierra'),

            ('entregas', 'Entregas consulta'),
            ('entregas_ok', 'Entrega OK'),
            ('entregas_cancela', 'Entrega cancelada'),

            ('reasignar', 'Reasignar'),

            ('consultas_seguimiento', 'Consulta de seguimiento'),
            ('consultas_reporte_dia', 'Consulta de reporte del día'),

            ('catalogo', 'Catálogo consulta'),
            ('catalogo_agregar', 'Catálogo Agrega'),
            ('catalogo_modificar', 'Catáogo Modifica'),

            ('accesos', 'Accesos consulta'),
            ('accesos_modificar', 'Accesos modifica'),

            ('abrir', 'Día abre'),
            ('cerrar', 'Día cierra'),

            ('usuarios', 'Usuarios consulta'),
            ('crea_usuario', 'Usuario nuevo'),
            ('modifica_usuario', 'Usuario modifica'),
        )


    def ensure_single_open_status(sender, instance, **kwargs):
        if instance.estatus == 1:
            Contable.objects.exclude(id=instance.id).update(estatus=0)
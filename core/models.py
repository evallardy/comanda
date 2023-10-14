from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models

from usuario.models import Usuario

ACTIVO_CAJA = (
    (0, 'Cancelado'),
    (1, 'Por pagar'),
    (2, 'Pagado'),
)
ACTIVA_COMANDA = (
    (0, 'Cancelado'),
    (1, 'Actva'),
    (2, 'Pre-pagada'),
    (3, 'Cerrada'),
    (4, 'Cerrada sin pagar'),
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
ACTIVO_PROMOCION = (
    (0, 'No presentar'),
    (1, 'Presentar'),
)
ESTATUS_CONTABLE = (
    (0, 'Cerrado'),
    (1, 'Abierto'),
)
TIPO = (
    (1, 'Combo'),
    (2, 'Promoción'),
)
TIPO_PRODUCTO = (
    (1, 'Cocina'),
    (2, 'Bar'),
)
TIPO_SOLICITUD = (
    (1, 'Forzoso'),
    (2, 'Solo Uno'),
    (3, 'Opcional'),
)
TIPO_DICT = {
    descripcion: valor for valor, descripcion in TIPO_SOLICITUD
}
SINO = (
    (0, 'NO'),
    (1, 'SI'),
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
            ('servicio_ver', 'Comanda detalle'),
            ('servicio_mod', 'Comanda detalle mod.'),
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

            ('caja', 'Pago de comandas'),
        )


    def ensure_single_open_status(sender, instance, **kwargs):
        if instance.estatus == 1:
            Contable.objects.exclude(id=instance.id).update(estatus=0)
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db import models

from usuario.models import Usuario

ACTIVO_CAJA = (
    (0, 'Cancelado'),
    (1, 'Por pagar'),
    (2, 'Pagado'),
)
ACTIVO_CLIENTE = (
    (0, 'Cancelado'),
    (1, 'Activo'),
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
cartas = (
    (1, 'El gallo'),
    (2, 'El diablito'),
    (3, 'La dama'),
    (4, 'El catrín'),
    (5, 'El paraguas'),
    (6, 'La sirena'),
    (7, 'La escalera'),
    (8, 'La botella'),
    (9, 'El barril'),
    (10, 'El árbol'),
    (11, 'El melón'),
    (12, 'El valiente'),
    (13, 'El gorrito'),
    (14, 'La muerte'),
    (15, 'La pera'),
    (16, 'La bandera'),
    (17, 'El bandolón'),
    (18, 'El violoncello'),
    (19, 'La garza'),
    (20, 'El pájaro'),
    (21, 'La mano'),
    (22, 'La bota'),
    (23, 'La luna'),
    (24, 'El cotorro'),
    (25, 'El borracho'),
    (26, 'El negrito'),
    (27, 'El corazón'),
    (28, 'La sandía'),
    (29, 'El tambor'),
    (30, 'El camarón'),
    (31, 'Las jaras'),
    (32, 'El músico'),
    (33, 'La araña'),
    (34, 'El soldado'),
    (35, 'La estrella'),
    (36, 'El cazo'),
    (37, 'El mundo'),
    (38, 'El apache'),
    (39, 'El nopal'),
    (40, 'El alacrán'),
    (41, 'La rosa'),
    (42, 'La calavera'),
    (43, 'La campana'),
    (44, 'El cantarito'),
    (45, 'El venado'),
    (46, 'El sol'),
    (47, 'La corona'),
    (48, 'La chalupa'),
    (49, 'El pino'),
    (50, 'El pescado'),
    (51, 'La palma'),
    (52, 'La maceta'),
    (53, 'El arpa'),
    (54, 'La rana')
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
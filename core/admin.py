from django.contrib import admin

from pedido.models import *
from producto.models import *
from usuario.models import Usuario
from core.models import Contable
from loteria.models import *

admin.site.register(Comanda)
admin.site.register(Detalle)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Contable)
admin.site.register(Insumo)
admin.site.register(Grupo)
admin.site.register(Caja)
admin.site.register(Sorteo)
admin.site.register(Cliente)
admin.site.register(Cliente_comanda)
admin.site.register(Tabla_bingo)



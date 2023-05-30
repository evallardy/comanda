from django.contrib import admin

from pedido.models import Comanda, Detalle
from producto.models import Producto
from usuario.models import Usuario
from core.models import Contable

admin.site.register(Comanda)
admin.site.register(Detalle)
admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(Contable)
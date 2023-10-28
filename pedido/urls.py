from django.urls import path
from .views import *

urlpatterns = [
    path('servicio/', servicio.as_view(), name='servicio'),
    path('comanda/', comanda.as_view(), name='comanda'),
    path('comanda_ver/<str:pk>/<int:tipo_pago>/', comanda_ver.as_view(), name='comanda_ver'),
    path('cancela_pedido/<int:id>/<int:tipo_pago>/', cancela_pedido, name='cancela_pedido'),
    path('valida_mesa/', valida_mesa.as_view(), name='valida_mesa'),
    path('comanda_detalle/<int:pk>/', comanda_detalle.as_view(), name='comanda_detalle'),
    path('cancela_producto/<int:id>/', cancela_producto, name='cancela_producto'),
    path('mod_insumos/<int:numero>/', mod_insumos, name='mod_insumos'),
    path('comanda_surte/<str:pk>/', comanda_surte.as_view(), name='comanda_surte'),
    path('cocina/', cocina.as_view(), name='cocina'),
    path('bar/', bar.as_view(), name='bar'),
    path('termina_cocina/<id>/', termina_cocina, name='termina_cocina'),
    path('cancela_prod/<id>/<pantalla>/', cancela_prod, name='cancela_prod'),
    path('termina_bar/<id>/', termina_bar, name='termina_bar'),
    path('cancela_producto_bar/<id>/', cancela_producto_bar, name='cancela_producto_bar'),
    path('cancela_producto_cocina/<id>/', cancela_producto_cocina, name='cancela_producto_cocina'),
    path('cancela_producto_entrega/<id>/', cancela_producto_entrega, name='cancela_producto_entrega'),
    path('entregas/', entregas.as_view(), name='entregas'),
    path('termina_entrega/<id>/', termina_entrega, name='termina_entrega'),
    path('cobranza/', cobranza.as_view(), name='cobranza'),
    path('reasignar/', reasignar.as_view(), name='reasignar'),
    path('mesas/', mesas, name='mesas'),
    path('cancela_producto_reasignar/<int:id>/', cancela_producto_reasignar, name='cancela_producto_reasignar'),    
    path('reasignar_producto/<id_comanda>/<id_producto>/', reasignar_producto, name='reasignar_producto'),
    path('pago_comanda/<str:pk>/', pago_comanda.as_view(), name='pago_comanda'),
    path('pago_productos/', pago_productos, name='pago_productos'),
    path('cierra/<pk>/', cierra, name='cierra'),
    

#    path('comanda_nueva/<str:mesa>/<str:observacion>/', comanda_nueva.as_view(), name='comanda_nueva'),
#    path('comanda_nueva/<str:mesa>/', comanda_nueva.as_view(), name='comanda_nueva'),
#    path('comanda_surte/<str:mesa>/<str:pk>/', comanda_surte.as_view(), name='comanda_surte'),
#    path('producto/', producto.as_view(), name='producto'),
#    path('obtener_json_producto/<int:producto_id>/', obtener_json_producto, name='obtener_json_producto'),
#    path('obtener_json_cerveza/<int:producto_id>/', obtener_json_cerveza, name='obtener_json_cerveza'),
#    path('obtener_json_escarcha/<int:producto_id>/', obtener_json_escarcha, name='obtener_json_escarcha'),
#    path('obtener_json_complemento/<int:producto_id>/', obtener_json_complemento, name='obtener_json_complemento'),
#    path('obtener_json_carne/<int:producto_id>/', obtener_json_carne, name='obtener_json_carne'),
#    path('obtener_json_sazonador/<int:producto_id>/', obtener_json_sazonador, name='obtener_json_sazonador#'),

#    path('cancela_elaborado/<id>/<pantalla>/', cancela_elaborado, name='cancela_elaborado'),
#    path('reasigna/<id>/<comanda>/', reasigna, name='reasigna'),
#    path('reasigna_act/', reasigna_act, name='reasigna_act'),
#    path('pago_productos/', pago_productos, name='pago_productos'),
#    path('cancela_comanda/<pk>/', cancela_comanda, name='cancela_comanda'),
#    path('cierra_comanda/<pk>/', cierra_comanda, name='cierra_comanda'),
#    path('comanda_cliente/', comanda_cliente.as_view(), name='comanda_cliente'),
#    path('asigna_comanda/<cliente>/<comanda>/', asigna_comanda, name='asigna_comanda'),
#    path('comanda_surte_cliente/<str:pk>/', comanda_surte_cliente.as_view(), name='comanda_surte_cliente'),

    
    
#    path('comandas/update-status/', update_comanda_status, name='update_comanda_status'),
]
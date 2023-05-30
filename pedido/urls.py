from django.urls import path
from .views import *

urlpatterns = [
    path('cocina/', cocina.as_view(), name='cocina'),
    path('bar/', bar.as_view(), name='bar'),
    path('entregas/', entregas.as_view(), name='entregas'),
    path('reasignar/', reasignar.as_view(), name='reasignar'),
    path('comandas/update-status/', update_comanda_status, name='update_comanda_status'),
    path('servicio/', servicio.as_view(), name='servicio'),
    path('comanda/', comanda.as_view(), name='comanda'),
    path('comanda_nueva/<str:mesa>/<str:observacion>/', comanda_nueva.as_view(), name='comanda_nueva'),
    path('comanda_nueva/<str:mesa>/', comanda_nueva.as_view(), name='comanda_nueva'),
    path('comanda_surte/<str:mesa>/<str:observacion>/<str:pk>/', comanda_surte.as_view(), name='comanda_surte'),
    path('producto/', producto.as_view(), name='producto'),
    path('valida_mesa/', valida_mesa.as_view(), name='valida_mesa'),
    path('obtener_json_producto/<int:producto_id>/', obtener_json_producto, name='obtener_json_producto'),
    path('termina/<id>/<pantalla>/', termina, name='termina'),
    path('cancela_prod/<id>/<pantalla>/', cancela_prod, name='cancela_prod'),
    path('cancela_elaborado/<id>/<pantalla>/', cancela_elaborado, name='cancela_elaborado'),
    path('reasigna/<id>/<comanda>/', reasigna, name='reasigna'),
    path('reasigna_act/', reasigna_act, name='reasigna_act'),
    path('pagos/<str:pk>/', pagos.as_view(), name='pagos'),
    path('pago_productos/', pago_productos, name='pago_productos'),
    
]
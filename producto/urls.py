from django.urls import path
from producto.views import *

urlpatterns = [
    path('grupo_list/', GrupoListView.as_view(), name='grupo_list'),
    path('grupo_create/', GrupoCreateView.as_view(), name='grupo_create'),
    path('grupo_edit/<int:pk>/', GrupoUpdateView.as_view(), name='grupo_edit'),
    path('existencia/grupo/', existencia_grupo, name='existencia_grupo'),

    path('insumo_list/<pk>/<nombre>/', InsumoListView.as_view(), name='insumo_list'),
    path('insumo_create/<pk1>/<nombre>/', InsumoCreateView.as_view(), name='insumo_create'),
    path('insumo_edit/<pk>/<pk1>/<nombre>/', InsumoEditView.as_view(), name='insumo_edit'),
    path('existencia/insumo/', existencia_insumo, name='existencia_insumo'),

    path('producto_list/', producto_list.as_view(), name='producto_list'),
    path('crea_producto/', crea_producto.as_view(), name='crea_producto'),
    path('mod_producto/<pk>/', mod_producto.as_view(), name='mod_producto'),
    path('existencia/producto/', existencia_producto, name='existencia_producto'),
    path('lista/', lista, name='lista'),
    
    path('paquete_list/', paquete_list.as_view(), name='paquete_list'),
    path('crea_paquete/', crea_paquete.as_view(), name='crea_paquete'),
    path('mod_paquete/<pk>/', mod_paquete.as_view(), name='mod_paquete'),
    path('existencia/paquete/', existencia_paquete, name='existencia_paquete'),
]
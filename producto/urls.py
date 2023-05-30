from django.urls import path
from .views import *

urlpatterns = [
    path('producto_list/', producto_list.as_view(), name='producto_list'),
    path('crea_producto/', crea_producto.as_view(), name='crea_producto'),
    path('mod_producto/<pk>/', mod_producto.as_view(), name='mod_producto'),
]
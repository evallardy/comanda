from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'), 
    path('abre_dia/', abre_dia, name='abre_dia'),
    path('cierra_dia/', cierra_dia, name='cierra_dia'),
    path('consultas/', consultas, name='consultas'),
    path('seguimiento/', seguimiento.as_view(), name='seguimiento'),
    path('reporte_diario/', reporte_diario.as_view(), name='reporte_diario'),
    path('permisos_usuario/', permisos_usuario.as_view(), name='permisos_usuario'),
    path('todos_permisos/<id>/', todos_permisos, name='todos_permisos'),
    path('cambia_contrasena/', cambia_contrasena, name='cambia_contrasena'),
]
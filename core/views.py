from django.shortcuts import render, redirect
from django.views.generic import ListView
from datetime import date
from django.db.models import Count, Q, Sum

from core.models import Contable
from pedido.models import Comanda, Detalle

fecha_actual = date.today()

def index(request):
    template_name = 'core/index.html'
    context = {}
    fecha_contable = Contable.objects.filter(estatus=1).first()
    if fecha_contable:
        context['contable'] = fecha_contable.fecha
    else:
        context['contable'] = ''
    return render(request, template_name, context=context)

def abre_dia(request):
    usuario = request.user
    existe = Contable.objects.filter(fecha=fecha_actual).first()
    if existe:
        actualiza = Contable.objects.filter(fecha=fecha_actual).update(estatus=1, usuario_abre=usuario)
    else:
        nuevo_contable = Contable(
            fecha=fecha_actual,
            usuario_abre=usuario,
            estatus=1
        )
        nuevo_contable.save()
    context = {}
    fecha_contable = Contable.objects.filter(estatus=1).first()
    if fecha_contable:
        context['contable'] = fecha_contable.fecha
    else:
        context['contable'] = ''
    return render(request, 'core/index.html', context=context)

def cierra_dia(request):
    usuario = request.user
    Contable.objects.filter(estatus=1).update(estatus=0, usuario_cierra=usuario)
    return redirect('index')
#    return render(request, 'core/index.html')

def consultas(request):
    template_name = 'core/consultas.html'
    context = {}
    return render(request, template_name, context=context)

class seguimiento(ListView):
    model = Detalle
    template_name = 'core/seguimiento.html'
    context_object_name = 'seguimiento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = Comanda.objects.filter(estatus__in=[1,2,3], fecha_contable=fecha_contable) \
        .annotate( \
        cantidad_por_elaborar_bar=Count('detalle', filter=Q(detalle__estatus=1, detalle__producto__tipo=2)), \
        cantidad_por_elaborar_cocina=Count('detalle', filter=Q(detalle__estatus=1, detalle__producto__tipo=1)), \
        cantidad_por_entregar_bar=Count('detalle', filter=Q(detalle__estatus=2, detalle__producto__tipo=2)), \
        cantidad_por_entregar_cocina=Count('detalle', filter=Q(detalle__estatus=2, detalle__producto__tipo=1)), \
        cantidad_por_cobrar=Count('detalle', filter=Q(detalle__estatus=3)), \
        cantidad_pagados=Count('detalle', filter=Q(detalle__estatus=4)), \
        cantidad_por_reasignar_bar=Count('detalle', filter=Q(detalle__estatus=5, detalle__producto__tipo=2)), \
        cantidad_por_reasignar_cocina=Count('detalle', filter=Q(detalle__estatus=5, detalle__producto__tipo=1)), \
        cantidad_cancelados_bar=Count('detalle', filter=Q(detalle__estatus=6, detalle__producto__tipo=2)), \
        cantidad_cancelados_cocina=Count('detalle', filter=Q(detalle__estatus=6, detalle__producto__tipo=1)))
        return queryset

class reporte_diario(ListView):
    model = Detalle
    template_name = 'core/reporte_diario.html'
    context_object_name = 'reporte_diario'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = Comanda.objects.filter(estatus__in=[1,2,3], fecha_contable=fecha_contable) \
        .annotate( \
        importe_por_cobrar_bar=Sum('detalle__importe', filter=Q(detalle__estatus=3, detalle__producto__tipo=2)), \
        importe_por_cobrar_cocina=Sum('detalle__importe', filter=Q(detalle__estatus=3, detalle__producto__tipo=1)), \
        importe_por_cobrar=Sum('detalle__importe', filter=Q(detalle__estatus=3)), \
        importe_pagados_bar=Sum('detalle__importe', filter=Q(detalle__estatus=4, detalle__producto__tipo=2)), \
        importe_pagados_cocina=Sum('detalle__importe', filter=Q(detalle__estatus=4, detalle__producto__tipo=1)), \
        importe_pagados=Sum('detalle__importe', filter=Q(detalle__estatus=4)))
        return queryset

def fecha_contable_activa(self):
    contable = Contable.objects.filter(estatus=1).first()
    if contable:
        fecha_contable = contable.fecha
    else:
        fecha_contable = fecha_actual
    return fecha_contable

from django.views.generic import ListView, CreateView, UpdateView, TemplateView, FormView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Count, Q, Sum
from django.views.generic.detail import DetailView
from django.db import transaction
from django.views import View
from django.db import transaction
from django.template.loader import render_to_string
from django.core.cache import cache
import threading
import time
import json

from .models import *
from core.models import Contable
from .forms import *
from core.views import fecha_contable_activa

def update_comanda_status(request):
    if request.method == 'POST' and request.is_ajax():
        comanda_id = request.POST.get('comanda_id')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

def termina(request, id, pantalla):
    usuario = request.user
    id_detalle = id
    if pantalla == 'entregas':
        detalle = Detalle.objects.filter(id=id_detalle).update(estatus=3, usuario_entrega=usuario)
    else:
        detalle = Detalle.objects.filter(id=id_detalle).update(estatus=2, usuario_elabora=usuario)
    return redirect(pantalla)

def cancela_prod(request, id, pantalla):
    usuario = request.user
    id_detalle = id
    detalle = Detalle.objects.filter(id=id_detalle).update(estatus=0, usuario_cancela=usuario)
    return redirect(pantalla)

def cancela_elaborado(request, id, pantalla):
    usuario = request.user
    id_detalle = id
    with transaction.atomic():
        detalle = Detalle.objects.filter(id=id_detalle).update(estatus=5, usuario_cancela=usuario)
        detalle_original = Detalle.objects.get(id=id_detalle)
        detalle_original.crear_copia()
    return redirect(pantalla)

def reasigna(request, id, comanda):
    usuario = request.user
    id_detalle = id
    if comanda =='0':
        detalle = Detalle.objects.filter(id=id_detalle) \
            .update(estatus=6, usuario_reasigna=usuario)
    else:
        detalle = Detalle.objects.filter(id=id_detalle) \
            .update(estatus=2, usuario_reasigna=usuario, comanda_id=comanda)
    return redirect('reasignar')

def reasigna_act(request):
    return redirect('reasignar')

def obtener_json_producto(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        campos_adicionales = producto.ingredientes
        precio = producto.precio
        return JsonResponse({'campos_adicionales': campos_adicionales, 'precio': precio}, safe=False)
    except Producto.DoesNotExist:
        return JsonResponse({'campos_adicionales': [], 'precio': 0}, safe=False)

class cocina(ListView):
    model = Detalle
    template_name = 'pedido/cocina.html'
    context_object_name = 'cocina'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for detalle in context['cocina']:
            detalle.especificacion1 = json.loads(detalle.especificacion)
        return context

    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = Detalle.objects.filter(estatus=1, producto__tipo=1, comanda__fecha_contable=fecha_contable).order_by('fecha_alta')
        return queryset

class bar(ListView):
    model = Detalle
    template_name = 'pedido/bar.html'
    context_object_name = 'bar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for detalle in context['bar']:
            detalle.especificacion1 = json.loads(detalle.especificacion)
        return context

    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = Detalle.objects.filter(estatus=1, producto__tipo=2, comanda__fecha_contable=fecha_contable).order_by('fecha_alta')
        return queryset

class reasignar(ListView):
    model = Detalle
    template_name = 'pedido/reasignar.html'
    context_object_name = 'reasignar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesas_cmb'] = Comanda.objects.filter(estatus__in=[1,2])
        for detalle in context['reasignar']:
            detalle.especificacion1 = json.loads(detalle.especificacion)
        return context

    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = Detalle.objects.filter(estatus=5, comanda__fecha_contable=fecha_contable).order_by('fecha_alta')
        return queryset

class entregas(ListView):
    model = Detalle
    template_name = 'pedido/entregas.html'
    context_object_name = 'entregas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for detalle in context['entregas']:
            detalle.especificacion1 = json.loads(detalle.especificacion)
        return context

    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = Detalle.objects.filter(estatus=2, comanda__fecha_contable=fecha_contable).order_by('fecha_alta')
        return queryset

class servicio(ListView):
    model = Comanda
    template_name = 'pedido/servicio.html'
    context_object_name = 'servicio'
    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = Comanda.objects.filter(estatus__in=[1,2], fecha_contable=fecha_contable) \
        .annotate(cantidad_por_pagar=Count('detalle', filter=Q(detalle__estatus__in=[3])), \
        cantidad_recibidas=Count('detalle', filter=Q(detalle__estatus__in=[3,4])), \
        importe_por_pagar=Sum('detalle__importe', filter=Q(detalle__estatus=3)))
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class comanda(CreateView):
    model = Comanda
    form_class = ComandaForm
    template_name = 'pedido/comanda.html'
    success_url = reverse_lazy('index')
    def get_context_data(self, **kwargs):
        context = super(comanda, self).get_context_data(**kwargs)
        fecha_contable = fecha_contable_activa(self)
        context['activas'] = Comanda.objects.filter(estatus__in=[1,2], fecha_contable=fecha_contable)
        return context

class producto(CreateView):
    model = Detalle
    template_name = 'pedido/producto.html'
    context_object_name = 'producto'
    form_class = ProductoForm

class comanda_nueva(CreateView):
    model = Detalle
    form_class = DetalleForm
    template_name = 'pedido/detalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesa'] = self.kwargs.get('mesa')
        context['observacion'] = self.kwargs.get('observacion','')
        context['producto_cmb'] = Producto.objects.filter(estatus=1)
        fecha_contable = fecha_contable_activa(self)
        context['activas'] = Comanda.objects.filter(estatus__in=[1,2], fecha_contable=fecha_contable)
        context['usuario'] = self.request.user
        return context
    def post(self, request, *args, **kwargs):
        mesa = request.POST.get('mesa')
        observacion = request.POST.get('observacion')
        lista = request.POST.get('lista')
        lista_json = json.loads(lista)
        usuario = self.request.user
        with transaction.atomic():
            comanda = Comanda(mesa=mesa, observacion=observacion, usuario=usuario)
            comanda.save()
            num_comanda = comanda.id
            for item in lista_json:
                nombre = item['nombre']
                cantidad = item['cantidad']
                producto_id = item['productoId']
                precio = item['precio']
                importe = item['importe']
                json_elemento = item['jsonElemento']
                # Crear el detalle de la comanda
                detalle = Detalle(
                    comanda_id=num_comanda,
                    producto_id=producto_id,
                    nom_producto=nombre,
                    especificacion=json_elemento,
                    cantidad=cantidad,
                    precio_unitario=precio,
                    importe=importe,
                    usuario=usuario
                )
                detalle.save()
        return HttpResponseRedirect(reverse_lazy('servicio'))

class comanda_surte(CreateView):
    model = Detalle
    form_class = DetalleForm
    template_name = 'pedido/detalle_surte.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', '0')
        mesa = self.kwargs.get('mesa', '')
        observacion = self.kwargs.get('observacion', '')
        context['mesa'] = mesa
        context['observacion'] = observacion
        context['producto_cmb'] = Producto.objects.filter(estatus=1)
        fecha_contable = fecha_contable_activa(self)
        context['activas'] = Comanda.objects.filter(estatus__in=[1,2], fecha_contable=fecha_contable)
        context['usuario'] = self.request.user
        return context
    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', '0')
        mesa = self.kwargs.get('mesa', '')
        observacion = self.kwargs.get('observacion', '')
        lista = request.POST.get('lista')
        lista_json = json.loads(lista)
        usuario = self.request.user
        with transaction.atomic():
            num_comanda = pk
            for item in lista_json:
                nombre = item['nombre']
                cantidad = item['cantidad']
                producto_id = item['productoId']
                precio = item['precio']
                importe = item['importe']
                json_elemento = item['jsonElemento']
                # Crear el detalle de la comanda
                detalle = Detalle(
                    comanda_id=num_comanda,
                    producto_id=producto_id,
                    nom_producto=nombre,
                    especificacion=json_elemento,
                    cantidad=cantidad,
                    precio_unitario=precio,
                    importe=importe,
                    usuario=usuario
                )
                detalle.save()
        return HttpResponseRedirect(reverse_lazy('servicio'))

class valida_mesa(View):
    def get(self, request):
        id_mesa = request.GET.get('id_mesa')
        fecha_contable = fecha_contable_activa(self)
        mesa = Comanda.objects.filter(mesa=id_mesa, fecha_contable=fecha_contable).first()
        if mesa:
            existe = True
        else:
            existe = False
        return JsonResponse({'existe': existe})

class pagos(ListView):
    model = Detalle
    template_name = 'pedido/pagos.html'
    context_object_name = 'pagos'
    def get_queryset(self):
        pk = self.kwargs.get('pk', '0')
        fecha_contable = fecha_contable_activa(self)
        queryset = Detalle.objects.filter(comanda_id=pk, estatus__in=[1,2,3,4], comanda__fecha_contable=fecha_contable)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(pagos, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', '0')
        fecha_contable = fecha_contable_activa(self)
        suma_importe = Detalle.objects.filter(comanda_id=pk, estatus__in=[2, 3, 4], comanda__fecha_contable=fecha_contable).aggregate(total_importe=Sum('importe'))
        total_importe = suma_importe['total_importe']
        total_importe = total_importe or 0
        context['total_importe'] = total_importe
        context['pk'] = pk
        return context

def pago_productos(request):
    if request.method == 'POST':
        datos = json.loads(request.POST.get('datos'))
        with transaction.atomic():
            for dato in datos:
                id_pago = dato['id']
                valor = dato['valor']
                registro_id = id_pago.split('_')[-1]
                detalle = Detalle.objects.get(id=registro_id)
                detalle.estatus = 4
                detalle.save()
    return HttpResponseRedirect(reverse_lazy('servicio'))
        

    
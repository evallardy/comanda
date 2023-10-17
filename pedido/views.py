from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, FormView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Count, Q, Sum, Subquery, F, ExpressionWrapper, IntegerField, FloatField
from django.views.generic.detail import DetailView
from django.views import View
from django.db import transaction
from django.template.loader import render_to_string
from django.core.cache import cache
from django.core import serializers
from itertools import chain
from django.db.models.functions import Coalesce
import threading
import time
import json
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseNotAllowed

from .models import *
from core.models import Contable
from .forms import *
from core.views import fecha_contable_activa
from producto.models import *
from producto.views import lista_productos, lista_paquetes

@login_required
def update_comanda_status(request):
    if request.method == 'POST' and request.is_ajax():
        comanda_id = request.POST.get('comanda_id')
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})

@login_required
def termina_cocina(request, id):
    usuario = request.user
    id_detalle = id
    detalle = Detalle.objects.filter(id=id_detalle).update(estatus=2, usuario_elabora=usuario)
    return redirect('cocina')

@login_required
def termina_bar(request, id):
    usuario = request.user
    id_detalle = id
    detalle = Detalle.objects.filter(id=id_detalle).update(estatus=2, usuario_elabora=usuario)
    return redirect('bar')

@login_required
def termina_entrega(request, id):
    usuario = request.user
    id_detalle = id
    detalle = Detalle.objects.filter(id=id_detalle).update(estatus=3, usuario_elabora=usuario)
    return redirect('entregas')

@login_required
def cancela_comanda(request, pk):
    usuario = request.user
    id_comanda = pk
    comanda = Comanda.objects.filter(id=id_comanda).update(estatus=0, usuario_cancela=usuario)
    return redirect('servicio')

@login_required
def cierra_comanda(request, pk):
    usuario = request.user
    id_comanda = pk
    comanda = Comanda.objects.filter(id=id_comanda).update(estatus=3, usuario_cierra=usuario)
    return redirect('servicio')

@login_required
def cancela_prod(request, id, pantalla):
    usuario = request.user
    id_detalle = id
    detalle = Detalle.objects.filter(id=id_detalle).update(estatus=0, usuario_cancela=usuario)
    return redirect(pantalla)

@login_required
def cancela_elaborado(request, id, pantalla):
    usuario = request.user
    id_detalle = id
    with transaction.atomic():
        detalle = Detalle.objects.filter(id=id_detalle).update(estatus=5, usuario_cancela=usuario)
        detalle_original = Detalle.objects.get(id=id_detalle)
        detalle_original.crear_copia()
    return redirect(pantalla)

@login_required
def reasigna_act(request):
    return redirect('reasignar')

@login_required
def obtener_json_producto(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        campos_adicionales = producto.ingredientes
        breve = producto.breve
        precio = producto.precio
        return JsonResponse({'campos_adicionales': campos_adicionales, 'precio': precio, 'breve': breve}, safe=False)
    except Producto.DoesNotExist:
        return JsonResponse({'campos_adicionales': [], 'precio': 0, 'breve': ''}, safe=False)

@login_required
def obtener_json_cerveza(request, producto_id):
    producto = Producto.objects.filter(id=producto_id).first()
    if producto.cerveza == 1:
        try:
            cervezas = Cerveza.objects.filter(estatus=1)
            campos_json = serializers.serialize('json', cervezas)
            campos_adicionales = json.dumps(json.loads(campos_json), indent=4)
            return JsonResponse({'campos_adicionales': campos_adicionales,}, safe=False)
        except Producto.DoesNotExist:
            return JsonResponse({'campos_adicionales': [],}, safe=False)
    else:
        return JsonResponse({'campos_adicionales': [],}, safe=False)

@login_required
def obtener_json_escarcha(request, producto_id):
    producto = Producto.objects.filter(id=producto_id).first()
    if producto.escarcha == 1:
        try:
            escarcha = Escarcha.objects.filter(estatus=1)
            campos_json = serializers.serialize('json', escarcha)
            campos_adicionales = json.dumps(json.loads(campos_json), indent=4)
            return JsonResponse({'campos_adicionales': campos_adicionales,}, safe=False)
        except Producto.DoesNotExist:
            return JsonResponse({'campos_adicionales': [],}, safe=False)
    else:
        return JsonResponse({'campos_adicionales': [],}, safe=False)

@login_required
def obtener_json_complemento(request, producto_id):
    producto = Producto.objects.filter(id=producto_id).first()
    if producto.complemento == 1:
        try:
            complemento = Complemento.objects.filter(estatus=1)
            campos_json = serializers.serialize('json', complemento)
            campos_adicionales = json.dumps(json.loads(campos_json), indent=4)
            return JsonResponse({'campos_adicionales': campos_adicionales,}, safe=False)
        except Producto.DoesNotExist:
            return JsonResponse({'campos_adicionales': [],}, safe=False)
    else:
        return JsonResponse({'campos_adicionales': [],}, safe=False)

@login_required
def obtener_json_carne(request, producto_id):
    producto = Producto.objects.filter(id=producto_id).first()
    if producto.carne == 1:
        try:
            carne = Carne.objects.filter(estatus=1)
            campos_json = serializers.serialize('json', carne)
            campos_adicionales = json.dumps(json.loads(campos_json), indent=4)
            return JsonResponse({'campos_adicionales': campos_adicionales,}, safe=False)
        except Producto.DoesNotExist:
            return JsonResponse({'campos_adicionales': [],}, safe=False)
    else:
        return JsonResponse({'campos_adicionales': [],}, safe=False)

@login_required
def obtener_json_sazonador(request, producto_id):
    producto = Producto.objects.filter(id=producto_id).first()
    if producto.sazonador == 1:
        try:
            sazonador = Sazona.objects.filter(estatus=1)
            campos_json = serializers.serialize('json', sazonador)
            campos_adicionales = json.dumps(json.loads(campos_json), indent=4)
            return JsonResponse({'campos_adicionales': campos_adicionales,}, safe=False)
        except Producto.DoesNotExist:
            return JsonResponse({'campos_adicionales': [],}, safe=False)
    else:
        return JsonResponse({'campos_adicionales': [],}, safe=False)

@login_required
def pago_productos(request):
    if request.method == 'POST':
        datos = json.loads(request.POST.get('datos'))
        with transaction.atomic():
            for dato in datos:
                id_pago = dato['id']
                valor = dato['valor']
                registro_id = id_pago.split('_')[-1]
                caja = Caja.objects.filter(id=registro_id) \
                    .update(estatus=2, usuario_cobra=request.user)
                detalle = Detalle.objects.filter(caja_id=registro_id) \
                    .update(estatus=4, usuario_cobra=request.user)
    return HttpResponseRedirect(reverse_lazy('index'))

@login_required
def asigna_comanda(request, cliente, comanda):
    comanda = Comanda.objects.filter(id=comanda).update(usuario_cliente_id=cliente)

def mod_insumos(request, numero):
    if request.method == 'POST':
        data = json.loads(request.body)
        insumos_json = json.loads(data.get('seleccionJSON'))
        insumos = Detalle.objects.filter(id=numero).update(especificacion=insumos_json)
        if insumos:
            actualizo = True
        else:
            actualizo = False
        return JsonResponse({'actualizo': actualizo,})

class servicio(LoginRequiredMixin, ListView):
    model = Comanda
    template_name = 'pedido/servicio.html'
    context_object_name = 'servicio'
    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset1 = Comanda.objects.filter( 
            estatus__in=[1, 2, 3], 
            fecha_contable=fecha_contable 
        ).annotate( 
            importe_total=Sum('caja__importe', filter=Q(caja__estatus__in=[1, 2, 3, 4])), 
            producto_total=Count('caja', filter=Q(caja__estatus=1000)),
            producto_cancelado=Count('caja', filter=Q(caja__estatus=1000)),
        )
        queryset2 = Comanda.objects.filter(
            estatus__in=[1, 2, 3],
            fecha_contable=fecha_contable
        ).annotate(
            importe_total=Count('caja', filter=Q(caja__estatus=1000)),
            producto_total=Count('caja__detalle', filter=Q(caja__detalle__estatus__in=[1, 2, 3, 4])),
            producto_cancelado=Count('caja__detalle', filter=Q(caja__detalle__estatus__in=[0, 5, 6]))
        )
        queryset1 = queryset1.values('id', 'mesa', 'observacion', 'importe_total', 'producto_total', 'producto_cancelado')
        queryset2 = queryset2.values('id', 'mesa', 'observacion', 'importe_total', 'producto_total', 'producto_cancelado')
        queryset3 = queryset1.union(queryset2).order_by('id')
        datos = []
        llave = 0
        for comanda in queryset3:
            if comanda['importe_total'] is None:
                importe_total = 0
            else:
                importe_total = comanda['importe_total']
            if comanda['producto_total'] is None:
                producto_total = 0
            else:
                producto_total = comanda['producto_total']
            if comanda['producto_cancelado'] is None:
                producto_cancelado = 0
            else:
                producto_cancelado = comanda['producto_cancelado']
            if llave == comanda['id']:
                registro['importe_total'] += importe_total
                registro['producto_total'] += producto_total
                registro['producto_cancelado'] += producto_cancelado
                datos.append(registro)
            else:                
                registro = {
                    'id': comanda['id'],
                    'mesa': comanda['mesa'],
                    'observacion': comanda['observacion'],
                    'importe_total': importe_total,
                    'producto_total': producto_total,
                    'producto_cancelado': producto_cancelado
                }
                llave = comanda['id']
        queryset = datos
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicio_perm'] = self.request.user.has_perm('core.servicio')
        context['servicio_nueva_perm'] = self.request.user.has_perm('core.servicio_nueva')
        context['servicio_solicitar_perm'] = self.request.user.has_perm('core.servicio_solicitar')
        context['servicio_cancelar_perm'] = self.request.user.has_perm('core.servicio_cancelar')
        context['servicio_pagar_perm'] = self.request.user.has_perm('core.servicio_pagar')
        context['servicio_ver_perm'] = self.request.user.has_perm('core.servicio_ver')
        context['servicio_cierra_perm'] = self.request.user.has_perm('core.servicio_cierra')
        
        context['lt_paquetes'] = lista_paquetes  
        context['lt_productos'] = lista_productos
        return context

class comanda(LoginRequiredMixin, FormView):
    model = Comanda
    form_class = ComandaForm    
    template_name = 'pedido/comanda.html'
    def get_context_data(self, **kwargs):
        context = super(comanda, self).get_context_data(**kwargs)
        fecha_contable = fecha_contable_activa(self)
        context['activas'] = Comanda.objects.filter(estatus__in=[1,2], fecha_contable=fecha_contable)
        context['producto_cmb'] = lista_productos
        context['paquete_cmb'] = lista_paquetes
        return context
    def post(self, request, *args, **kwargs):
        usuario = request.user
        mesa = request.POST.get('mesa')
        observacion = request.POST.get('observacion')
        pedido = request.POST.get('pedido')
        if pedido:
            pedido_json = json.loads(pedido)
            fecha_contable = fecha_contable_activa(self)
            with transaction.atomic():
                comanda = Comanda(
                    mesa = mesa,
                    observacion = observacion,
                    usuario = usuario,
                    fecha_contable = fecha_contable,
                )
                comanda.save()
                for producto in pedido_json:
                    if producto['cobrar_caja'] == 'Caja':
                        importe = producto['cantidad'] * producto['precio']
                        precio = producto['precio']
                        if producto['nombre_paquete'] == '':
                            especifico = producto['nombre_producto']
                        else:
                             especifico = producto['nombre_paquete']
                        caja = Caja(
                            comanda_id = comanda.id,
                            descripcion = producto['especificacion'],
                            especifico = especifico,
                            cantidad = producto['cantidad'],
                            precio_unitario = precio,
                            importe = importe,
                            usuario_elabora = usuario,
                            fecha_contable = fecha_contable
                        )
                        caja.save()
                    else:
                        precio = 0
                    detalle = Detalle(
                        caja_id = caja.id,
                        producto_id = producto['producto_id'],
                        nom_paquete = producto['nombre_paquete'],
                        nom_producto = producto['nombre_producto'],
                        especifico = producto['especificacion'],
                        cantidad = 1,
                        precio_unitario = precio,
                        importe = precio,
                        usuario = usuario,
                        fecha_contable = fecha_contable
                    )
                    detalle.save()
                    insumos_lista = []
                    insumos = json.dumps(producto['solicitado_json'])
                    insumos_json = json.loads(insumos)
                    for insumo in insumos_json:
                        insumos_mat = {
                            'id': insumo['id'],
                            'nombre_grupo': insumo['nombre_grupo'],
                            'nombre_insumo': insumo['nombre_insumo'],
                            'opcion': insumo['opcion'],
                            'pedir': insumo['pedir'],
                        }
                        insumos_lista.append(insumos_mat)
                    detalle_insumo = Detalle.objects.filter(id=detalle.id).update(especificacion=insumos_lista)
        return HttpResponseRedirect(reverse_lazy('servicio'))

class producto(LoginRequiredMixin, CreateView):
    model = Detalle
    template_name = 'pedido/producto.html'
    context_object_name = 'producto'
    form_class = ProductoForm

class comanda_nueva(LoginRequiredMixin, CreateView):
    model = Detalle
    form_class = DetalleForm
    template_name = 'pedido/detalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mesa'] = self.kwargs.get('mesa')
        context['observacion'] = self.kwargs.get('observacion','')
        context['producto_cmb'] = lista_productos
        fecha_contable = fecha_contable_activa(self)
        context['activas'] = Comanda.objects.filter(estatus__in=[1,2], fecha_contable=fecha_contable)
        context['usuario'] = self.request.user
        return context
    def post(self, request, *args, **kwargs):
        mesa = request.POST.get('mesa')
        observacion = request.POST.get('observacion')
        lista = request.POST.get('lista')
        if lista:
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

class comanda_surte(LoginRequiredMixin, FormView):
    model = Comanda
    form_class = ComandaForm    
    template_name = 'pedido/comanda_surte.html'
    def get_context_data(self, **kwargs):
        context = super(comanda_surte, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        comanda = Comanda.objects.filter(id=pk).first()
        if comanda:
            mesa = comanda.mesa
            observacion = comanda.observacion
        else:
            mesa = 0
            observacion = ''
        fecha_contable = fecha_contable_activa(self)
        context['mesa'] = mesa
        context['observacion'] = observacion
        context['activas'] = Comanda.objects.filter(estatus__in=[1,2], fecha_contable=fecha_contable)
        context['producto_cmb'] = lista_productos
        context['paquete_cmb'] = lista_paquetes
        return context
    def post(self, request, *args, **kwargs):
        usuario = request.user
        pk = self.kwargs.get('pk')
        pedido = request.POST.get('pedido')
        if pedido:
            pedido_json = json.loads(pedido)
            fecha_contable = fecha_contable_activa(self)
            with transaction.atomic():
                for producto in pedido_json:
                    if producto['cobrar_caja'] == 'Caja':
                        importe = producto['cantidad'] * producto['precio']
                        precio = producto['precio']
                        if producto['nombre_paquete'] == '':
                            especifico = producto['nombre_producto']
                        else:
                             especifico = producto['nombre_paquete']
                        caja = Caja(
                            comanda_id = pk,
                            descripcion = producto['especificacion'],
                            especifico = especifico,
                            cantidad = producto['cantidad'],
                            precio_unitario = precio,
                            importe = importe,
                            usuario_elabora = usuario,
                            fecha_contable = fecha_contable
                        )
                        caja.save()
                    else:
                        precio = 0
                    detalle = Detalle(
                        caja_id = caja.id,
                        producto_id = producto['producto_id'],
                        nom_paquete = producto['nombre_paquete'],
                        nom_producto = producto['nombre_producto'],
                        especifico = producto['especificacion'],
                        cantidad = 1,
                        precio_unitario = precio,
                        importe = precio,
                        usuario = usuario,
                        fecha_contable = fecha_contable
                    )
                    detalle.save()
                    insumos_lista = []
                    insumos = json.dumps(producto['solicitado_json'])
                    insumos_json = json.loads(insumos)
                    for insumo in insumos_json:
                        insumos_mat = {
                            'id': insumo['id'],
                            'nombre_grupo': insumo['nombre_grupo'],
                            'nombre_insumo': insumo['nombre_insumo'],
                            'opcion': insumo['opcion'],
                            'pedir': insumo['pedir'],
                        }
                        insumos_lista.append(insumos_mat)
                    detalle_insumo = Detalle.objects.filter(id=detalle.id).update(especificacion=insumos_lista)
        return HttpResponseRedirect(reverse_lazy('servicio'))

class valida_mesa(LoginRequiredMixin, View):
    def get(self, request):
        id_mesa = request.GET.get('id_mesa')
        fecha_contable = fecha_contable_activa(self)
        mesa = Comanda.objects.filter(mesa=id_mesa, fecha_contable=fecha_contable).first()
        if mesa:
            existe = True
        else:
            existe = False
        return JsonResponse({'existe': existe})

class pago_comanda(LoginRequiredMixin, ListView):
    model = Detalle
    template_name = 'pedido/pago_comanda.html'
    context_object_name = 'pagos'
    success_url = reverse_lazy('cobranza')
    def get_queryset(self):
        pk = self.kwargs.get('pk', '0')
        fecha_contable = fecha_contable_activa(self)
        queryset = Caja.objects \
            .filter(comanda_id=pk, estatus__in=[1,2], comanda__fecha_contable=fecha_contable) \
            .annotate(
                productos_no_entregados=Count('detalle', filter=Q(detalle__estatus__in=[1,2])),
                productos_entregados=Count('detalle', filter=Q(detalle__estatus=3)),
        )
        return queryset
    def get_context_data(self, **kwargs):
        context = super(pago_comanda, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', '0')
        fecha_contable = fecha_contable_activa(self)
        importe_por_pagar = 0
        importe_pagado = 0

        cajas = Caja.objects.filter(comanda_id=pk)
        for caja in cajas:
            detalles = Detalle.objects.filter(caja_id=caja.id) \
                .order_by('caja_id')
            b_por_entregar = False
            b_entregado = False
            b_pagado = False
            for detalle in detalles:
                if detalle.estatus in [1,2]:
                    b_por_entregar = True
                if detalle.estatus == 3:
                    b_entregado = True
                if detalle.estatus == 4:
                    b_pagado = True
            if b_pagado:
                importe_pagado += caja.importe
            elif not b_por_entregar and b_entregado:
                importe_por_pagar += caja.importe
        context['importe_por_pagar'] = importe_por_pagar
        context['importe_pagado'] = importe_pagado
        context['pk'] = pk
        return context

class comanda_ver(LoginRequiredMixin, ListView):
    model = Detalle
    template_name = 'pedido/comanda_ver.html'
    context_object_name = 'pagos'
    def get_queryset(self):
        pk = self.kwargs.get('pk', '0')
        tipo_pago = self.kwargs.get('tipo_pago', 0)
        fecha_contable = fecha_contable_activa(self)
        if tipo_pago == 1:
            productos_por_pago = [1,2]
        elif tipo_pago == 2:
            productos_por_pago = [3]
        elif tipo_pago == 3:
            productos_por_pago = [4]
        else:
            productos_por_pago = 0
        queryset = Caja.objects.filter(comanda_id=pk, estatus__in=productos_por_pago, 
            comanda__fecha_contable=fecha_contable) \
            .annotate(elaborados=Count('detalle', filter=(~Q(detalle__estatus=1))))
        return queryset
    def get_context_data(self, **kwargs):
        context = super(comanda_ver, self).get_context_data(**kwargs)
        fecha_contable = fecha_contable_activa(self)
        pk = self.kwargs.get('pk', '0')
        tipo_pago = self.kwargs.get('tipo_pago', 0)
        if tipo_pago == 1:
            productos_por_pago = [1,2]
        elif tipo_pago == 2:
            productos_por_pago = [3]
        elif tipo_pago == 3:
            productos_por_pago = [4]
        else:
            productos_por_pago = 0
        context['tipo_pago'] = tipo_pago
        suma_importe = Caja.objects.filter(comanda_id=pk, estatus__in=productos_por_pago, comanda__fecha_contable=fecha_contable).aggregate(total_importe=Sum('importe'))
        mesa = Caja.objects.filter(comanda_id=pk).first()
        if mesa:
            mesa_id = mesa.comanda.mesa
        else:
            mesa_id = 0
        context['mesa_id'] = mesa_id
        total_importe = suma_importe['total_importe']
        total_importe = total_importe or 0
        context['total_importe'] = total_importe
        context['pk'] = pk
        comandas = Comanda.objects.filter(fecha_contable=fecha_contable, estatus__in=[1,2])
        registros_con_usuario = comandas.exclude(usuario_cliente__isnull=True).count()
        if registros_con_usuario > 0:
            clientes = Usuario.objects.filter(cliente=1).exclude(id__in=Subquery(comandas.values('usuario_cliente')))
        else:
            clientes = Usuario.objects.filter(cliente=1)
        context['clientes'] = clientes
        datos_comanda = Comanda.objects.filter(id=pk).first()
        if datos_comanda:
            cliente_asignado = datos_comanda.usuario_cliente_id
        else:
            cliente_asignado = 0
        context['cliente_asignado'] = cliente_asignado
        if cliente_asignado:
            datos_cliente_signado = Usuario.objects.filter(id=cliente_asignado).first()
            nombre_asigando = datos_cliente_signado.first_name + ' ' + datos_cliente_signado.last_name
            context['nombre_asigando'] = nombre_asigando
        return context

class comanda_cliente(LoginRequiredMixin, ListView):
    model = Detalle
    template_name = 'pedido/comanda_cliente.html'
    context_object_name = 'elementos'
    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        usuario = self.request.user
        queryset = Detalle.objects.filter(comanda__usuario_cliente=usuario.id, estatus__in=[1,2,3,4], comanda__fecha_contable=fecha_contable)
        return queryset
    def get_context_data(self, **kwargs):
        context = super(comanda_cliente, self).get_context_data(**kwargs)
        fecha_contable = fecha_contable_activa(self)
        usuario = self.request.user
        importe_pagado = Detalle.objects.filter(comanda__usuario_cliente=usuario.id, estatus=4, comanda__fecha_contable=fecha_contable).aggregate(total_importe=Sum('importe'))
        importe_por_pagar = Detalle.objects.filter(comanda__usuario_cliente=usuario.id, estatus__in=[1,2,3], comanda__fecha_contable=fecha_contable).aggregate(total_importe=Sum('importe'))
        importe_total = Detalle.objects.filter(comanda__usuario_cliente=usuario.id, estatus__in=[1,2,3,4], comanda__fecha_contable=fecha_contable).aggregate(total_importe=Sum('importe'))
        mesa = Comanda.objects.filter(usuario_cliente=usuario.id, fecha_contable=fecha_contable).first()
        mesa_id = mesa.mesa
        context['mesa_id'] = mesa_id
        context['importe_pagado'] = importe_pagado
        context['importe_por_pagar'] = importe_por_pagar
        context['importe_total'] = importe_total
        return context

class comanda_surte_cliente(LoginRequiredMixin, CreateView):
    model = Detalle
    form_class = DetalleForm
    template_name = 'pedido/detalle_surte_cliente.html'
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
        if lista:
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
        return HttpResponseRedirect(reverse_lazy('index'))

class comanda_detalle(LoginRequiredMixin, FormView):
    model = Detalle
    form_class = DetalleForm
    template_name = 'pedido/comanda_detalle.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        fecha_contable = fecha_contable_activa(self)
        context['pk'] = pk
        detalle = Detalle.objects.filter(caja__comanda_id=pk).order_by('id')
        mesa_id = detalle[0].caja.comanda.mesa
        context['mesa_id'] = mesa_id
        context['detalle'] = detalle
        context['nombre_usuario'] = self.request.user.first_name + ' ' + self.request.user.last_name
        context['servicio_mod_perm'] = self.request.user.has_perm('core.servicio_mod')
        context['servicio_cancelar_perm'] = self.request.user.has_perm('core.servicio_cancelar')
        totales = Caja.objects.filter(id=pk).first()
        if totales:
            context['total'] = totales.importe
            context['comanda_id'] = totales.comanda_id
        else:
            context['total'] = 0
            context['comanda_id'] = 0
        return context

class cobranza(LoginRequiredMixin, ListView):
    model = Caja
    template_name = 'pedido/cobranza.html'
    context_object_name = 'cobranza'
    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = Comanda.objects \
            .filter(fecha_contable=fecha_contable) \
            .annotate( \
                por_pagar=(Coalesce(Sum('caja__importe', filter=Q(caja__detalle__estatus=3)), \
                0.00, output_field=FloatField()) - \
                    Coalesce(Sum('caja__importe', filter=Q(caja__detalle__estatus__in=[1,2])),
                0.00, output_field=FloatField())), \
                pagado=(Sum('caja__importe', filter=Q(caja__estatus=2))), \
                por_pagar_real=(Sum('caja__importe', filter=Q(caja__estatus=1))), \
        )
        comandas = Comanda.objects.filter(fecha_contable=fecha_contable) \
            .order_by('fecha_alta')
        datos_ok = []
        for comanda in comandas:
            registro = {
                'id' : comanda.id,
                'mesa' : comanda.mesa,
                'observacion' : comanda.observacion,
                'pagado' : 0,
                'por_pagar' : 0
            }
            cajas = Caja.objects.filter(comanda_id=comanda.id) \
                .order_by('comanda_id')
            for caja in cajas:
                detalles = Detalle.objects.filter(caja_id=caja.id) \
                    .order_by('caja_id')
                b_por_entregar = False
                b_entregado = False
                b_pagado = False
                for detalle in detalles:
                    if detalle.estatus in [1,2]:
                        b_por_entregar = True
                    if detalle.estatus == 3:
                        b_entregado = True
                    if detalle.estatus == 4:
                        b_pagado = True
                if b_pagado:
                    registro['pagado'] += caja.importe
                elif not b_por_entregar and b_entregado:
                    registro['por_pagar'] += caja.importe
            datos_ok.append(registro)
        queryset = datos_ok 
        return queryset
    def get_context_data(self, **kwargs):
        context = super(cobranza, self).get_context_data(**kwargs)
        fecha_contable = fecha_contable_activa(self)
        context['servicio_cierra_perm'] = self.request.user.has_perm('core.servicio_cierra')
        return context

class cocina(LoginRequiredMixin, ListView):
    model = Detalle
    template_name = 'pedido/cocina.html'
    context_object_name = 'cocina'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cocina_perm'] = self.request.user.has_perm('core.cocina')
        context['cocina_termina_perm'] = self.request.user.has_perm('core.cocina_termina')
        context['cocina_cancela_perm'] = self.request.user.has_perm('core.cocina_cancela')
        return context
    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = detalle_x_grupo(1, 1)
        return queryset

class bar(LoginRequiredMixin, ListView):
    model = Detalle
    template_name = 'pedido/bar.html'
    context_object_name = 'bar'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bar_perm'] = self.request.user.has_perm('core.bar')
        context['bar_termina_perm'] = self.request.user.has_perm('core.bar_termina')
        context['bar_cancela_perm'] = self.request.user.has_perm('core.bar_cancela')
        return context
    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = detalle_x_grupo(1, 2)
        return queryset

class reasignar(LoginRequiredMixin, ListView):
    model = Detalle
    template_name = 'pedido/reasignar.html'
    context_object_name = 'reasignar'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reasignar_perm'] = self.request.user.has_perm('core.entregas')
        context['reasignar_termina_perm'] = self.request.user.has_perm('core.entregas_ok')
        context['reasignar_cancela_perm'] = self.request.user.has_perm('core.entregas_cancela')
        return context

    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = Detalle.objects.filter(estatus=5, caja__comanda__fecha_contable=fecha_contable).order_by('fecha_alta')
        return queryset

class entregas(LoginRequiredMixin, ListView):
    model = Detalle
    template_name = 'pedido/entregas.html'
    context_object_name = 'entregas'
    success_url = reverse_lazy('entregas')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entrega_perm'] = self.request.user.has_perm('core.entregas')
        context['entrega_termina_perm'] = self.request.user.has_perm('core.entregas_ok')
        context['entrega_cancela_perm'] = self.request.user.has_perm('core.entregas_cancela')
        return context
    def get_queryset(self):
        fecha_contable = fecha_contable_activa(self)
        queryset = detalle_x_grupo(2, 0)
        return queryset

@login_required
def cancela_pedido(request, id, tipo_pago):
    if request.method == 'GET':
        caja_id = id
        detalles = Detalle.objects.filter(caja_id=caja_id)
        comanda_id = detalles[0].caja.comanda.id
        try:
            with transaction.atomic():
                for detalle in detalles:
                    if detalle.estatus == 1:
                        Detalle.objects.filter(id=detalle.id) \
                            .update(estatus=6, usuario_cancela=request.user)
                    elif detalle.estatus == 2:
                        Detalle.objects.filter(id=detalle.id) \
                            .update(estatus=5, usuario_cancela=request.user)
                    else:
                        raise Exception("¡No se puede cancelar, producto entregado o pagado!")
                Caja.objects.filter(id=caja_id).update(estatus=0, usuario_cancela=request.User)
        except Exception as e:
            print("Excepción:", str(e))
    url = reverse('comanda_ver', args=(comanda_id, tipo_pago))
    return redirect(url)

@login_required
def cancela_producto(request, id):
    if request.method == 'GET':
        detalle_id = id
        detalle = Detalle.objects.filter(id=detalle_id).first()
        caja_id = detalle.caja.id
        comanda_id = detalle.caja.comanda.id
        with transaction.atomic():
            if detalle.estatus == 1:
                Detalle.objects.filter(id=detalle.id).update(estatus=6,
                    usuario_cancela_id=request.user)
            elif detalle.estatus == 2:
                Detalle.objects.filter(id=detalle.id).update(estatus=5,
                    usuario_cancela_id=request.user)
            pedido = Caja.objects.filter(id=caja_id).first()
            cantidad = pedido.cantidad - 1
            if cantidad == 0:
                importe = 0
            else:
                importe = cantidad * pedido.precio_unitario
            productos_pedido = Detalle.objects.filter(caja_id=caja_id,
                estatus__in=[1,2,3,4])
            if productos_pedido:
                Caja.objects.filter(id=caja_id).update(cantidad=cantidad, 
                    importe=importe)
            else:
                Caja.objects.filter(id=caja_id).update(cantidad=cantidad, 
                    importe=importe, usuario_cancela_id=request.user, 
                    estatus=0)
        url = reverse('comanda_detalle', args=(comanda_id))
        return redirect(url)
    else:
        url = reverse('index')
        return redirect(url)

@login_required
def cancela_producto_bar(request, id):
    if request.method == 'GET':
        detalle_id = id
        detalle_unico = Detalle.objects.filter(id=detalle_id).first()
        caja_id = detalle_unico.caja.id
        detalle = Detalle.objects.filter(caja_id=caja_id)
        with transaction.atomic():
            for detalle_prodcuto in detalle:
                if detalle_prodcuto.estatus == 1:
                    Detalle.objects.filter(id=detalle_prodcuto.id).update(estatus=0,
                        usuario_cancela_id=request.user)
                elif detalle_prodcuto.estatus == 2:
                    Detalle.objects.filter(id=detalle_prodcuto.id).update(estatus=5,
                        usuario_cancela_id=request.user)
            Caja.objects.filter(id=caja_id).update(usuario_cancela_id=request.user, 
                estatus=0)
        url = reverse('bar')
        return redirect(url)
    else:
        url = reverse('index')
        return redirect(url)

@login_required
def cancela_producto_cocina(request, id):
    if request.method == 'GET':
        detalle_id = id
        detalle_unico = Detalle.objects.filter(id=detalle_id).first()
        caja_id = detalle_unico.caja.id
        detalle = Detalle.objects.filter(caja_id=caja_id)
        with transaction.atomic():
            for detalle_prodcuto in detalle:
                if detalle_prodcuto.estatus == 1:
                    Detalle.objects.filter(id=detalle_prodcuto.id).update(estatus=0,
                        usuario_cancela_id=request.user)
                elif detalle_prodcuto.estatus == 2:
                    Detalle.objects.filter(id=detalle_prodcuto.id).update(estatus=5,
                        usuario_cancela_id=request.user)
            Caja.objects.filter(id=caja_id).update(usuario_cancela_id=request.user, 
                estatus=0)
        url = reverse('cocina')
        return redirect(url)
    else:
        url = reverse('index')
        return redirect(url)

@login_required
def cancela_producto_entrega(request, id):
    if request.method == 'GET':
        detalle_id = id
        detalle_unico = Detalle.objects.filter(id=detalle_id).first()
        caja_id = detalle_unico.caja.id
        detalle = Detalle.objects.filter(caja_id=caja_id)
        with transaction.atomic():
            for detalle_prodcuto in detalle:
                if detalle_prodcuto.estatus == 1:
                    Detalle.objects.filter(id=detalle_prodcuto.id).update(estatus=0,
                        usuario_cancela_id=request.user)
                elif detalle_prodcuto.estatus == 2:
                    Detalle.objects.filter(id=detalle_prodcuto.id).update(estatus=5,
                        usuario_cancela_id=request.user)
            Caja.objects.filter(id=caja_id).update(usuario_cancela_id=request.user, 
                estatus=0)
        url = reverse('entregas')
        return redirect(url)
    else:
        url = reverse('index')
        return redirect(url)

@login_required
def cancela_producto_reasignar(request, id):
    if request.method == 'GET':
        detalle_id = id
        with transaction.atomic():
            Detalle.objects.filter(id=detalle_id).update(estatus=6,
                usuario_cancela_id=request.user)
        url = reverse('reasignar')
        return redirect(url)
    else:
        url = reverse('index')
        return redirect(url)

@login_required
@require_http_methods(["GET", "POST"])  # Solo permitir solicitudes GET y POST
def mesas(request):
    if request.method == 'GET':
        fecha_contable = fecha_contable_activa(request)
        mesas = Comanda.objects.filter(fecha_contable=fecha_contable, estatus__in=[1,2])
        listado = []
        for mesa in mesas:
            registro = {
                'id': mesa.id,
                'mesa': mesa.mesa,
                'observacion': mesa.observacion,
            }
            listado.append(registro)
        return JsonResponse({'listado': listado,})
    else:
        return HttpResponseNotAllowed(['GET'])  # Devolver un 405 Method Not Allowed para otras solicitudes HTTP

@login_required
def reasignar_producto(request, id_comanda, id_producto):
    if request.method == 'POST':
        fecha_contable = fecha_contable_activa(request)
        producto = Detalle.objects.filter(id=id_producto).first()
        producto_precio = Producto.objects.filter(id=producto.producto_id).first()
        precio_unitario = producto_precio.precio
        with transaction.atomic():
            caja = Caja(
                comanda_id = id_comanda,
                descripcion = 'Producto',
                especifico = producto.nom_producto,
                cantidad = 1,
                precio_unitario = precio_unitario,
                importe = precio_unitario,
                usuario_elabora = request.user,
                fecha_contable = fecha_contable
            )
            caja.save()
            producto_cambio = Detalle.objects.filter(id = id_producto) \
                .update(estatus=2, caja=caja.id, precio_unitario=precio_unitario,
                    cantidad=1, importe=precio_unitario, nombre_paquete='',
                    especifico='Producto', usuario_reasigna=request.user)
        url = reverse('reasignar')
        return redirect(url)
    else:
        url = reverse('index')
        return redirect(url)

def detalle_x_grupo(valor_estatus, valor_tipo):
    fecha_contable = fecha_contable_activa(0)
    if valor_tipo == 0:
        detalle = Detalle.objects \
            .filter(fecha_contable=fecha_contable, estatus=valor_estatus) \
            .order_by('fecha_alta')
    else:
        detalle = Detalle.objects \
            .filter(fecha_contable=fecha_contable, 
                    estatus=valor_estatus, 
                    producto__tipo=valor_tipo) \
            .order_by('fecha_alta')
    queryset1 = Detalle.objects \
    .filter(fecha_contable=fecha_contable) \
    .values('caja_id') \
    .annotate( 
        producto_total=Count('caja_id'),
        producto_sin_entregar=Count('caja_id', filter=Q(caja__estatus=1000)),
    )
    queryset2 = Detalle.objects \
    .filter(fecha_contable=fecha_contable) \
    .values('caja_id') \
    .annotate( 
        producto_total=Count('caja_id', filter=Q(caja__estatus=1000)),
        producto_sin_entregar=Count('caja_id', filter=Q(estatus__in=[1, 2])),
    )
    queryset1 = queryset1.values('caja_id', 'producto_total', 'producto_sin_entregar')
    queryset2 = queryset2.values('caja_id', 'producto_total', 'producto_sin_entregar')
    queryset3 = queryset1.union(queryset2).order_by('caja_id')
    datos = []
    llave = 0
    for comanda in queryset3:
        if llave == comanda['caja_id']:
            registro['producto_total'] += comanda['producto_total']
            registro['producto_sin_entregar'] += comanda['producto_sin_entregar']
            datos.append(registro)
        else:                
            registro = {
                'caja_id': comanda['caja_id'],
                'producto_total': comanda['producto_total'],
                'producto_sin_entregar': comanda['producto_sin_entregar'],

            }
            llave = comanda['caja_id']
    datos_ok = []
    for deta in detalle:
        for dato1 in datos:
            if deta.caja_id == dato1['caja_id']:
                registro = {
                    'id': deta.id,
                    'nom_producto': deta.nom_producto,
                    'especificacion': deta.especificacion,
                    'mesa': deta.caja.comanda.mesa,
                    'total': dato1['producto_total'],
                    'producto_sin_entregar': dato1['producto_sin_entregar']
                }
                datos_ok.append(registro)
                break
    return datos_ok

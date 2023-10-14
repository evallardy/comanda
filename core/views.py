from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from datetime import date
from django.db.models import Count, Q, Sum
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import Permission
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib import messages

from core.models import Contable
from pedido.models import Comanda, Detalle
from usuario.models import Usuario

fecha_actual = date.today()

def index(request):
    template_name = 'core/index.html'
    context = {}
    if request.user:
        usuario = request.user.id
        if usuario:
            cliente = request.user.cliente
            fecha_contable = Contable.objects.filter(estatus=1).first()
            if not fecha_contable:
                fecha_contable_actual = fecha_actual
            else:
                fecha_contable_actual = fecha_contable.fecha
            if cliente:
                comanda = Comanda.objects.filter(usuario_cliente=request.user.id, estatus__in=[1,2], fecha_contable=fecha_contable_actual).first()
                if comanda:
                    context['mesa'] = comanda.mesa
                    context['pk'] = comanda.id
                    context['observacion'] = comanda.observacion
                    context['cliente_perm'] = True
                else:
                    context['cliente_perm'] = False
            else:
                if fecha_contable:
                    context['contable'] = fecha_contable.fecha
                    context['cocina_perm'] = request.user.has_perm('core.cocina')
                    context['bar_perm'] = request.user.has_perm('core.bar')
                    context['servicio_perm'] = request.user.has_perm('core.servicio')
                    context['entregas_perm'] = request.user.has_perm('core.entregas')
                    context['reasignar_perm'] = request.user.has_perm('core.reasignar')
                    context['consultas_seguimiento_perm'] = request.user.has_perm('core.consultas_seguimiento')
                    context['consultas_reporte_dia_perm'] = request.user.has_perm('core.consultas_reporte_dia')
                    context['catalogo_perm'] = request.user.has_perm('core.catalogo')
                    context['usuarios_perm'] = request.user.has_perm('core.usuarios')
                    context['accesos_perm'] = request.user.has_perm('core.accesos')
                    context['cerrar_perm'] = request.user.has_perm('core.cerrar')
                    context['caja_perm'] = request.user.has_perm('core.caja')
                else:
                    context['abrir_perm'] = request.user.has_perm('core.abrir')
                    context['contable'] = ''
    return render(request, template_name, context=context)

@login_required
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
        context['contable'] = fecha_contable.fecha
        context['cocina_perm'] = request.user.has_perm('core.cocina')
        context['bar_perm'] = request.user.has_perm('core.bar')
        context['servicio_perm'] = request.user.has_perm('core.servicio')
        context['entregas_perm'] = request.user.has_perm('core.entregas')
        context['reasignar_perm'] = request.user.has_perm('core.reasignar')
        context['consultas_seguimiento_perm'] = request.user.has_perm('core.consultas_seguimiento')
        context['consultas_reporte_dia_perm'] = request.user.has_perm('core.consultas_reporte_dia')
        context['catalogo_perm'] = request.user.has_perm('core.catalogo')
        context['usuarios_perm'] = request.user.has_perm('core.usuarios')
        context['accesos_perm'] = request.user.has_perm('core.accesos')
        context['cerrar_perm'] = request.user.has_perm('core.cerrar')
    else:
        context['contable'] = ''
    return render(request, 'core/index.html', context=context)

@login_required
def cierra_dia(request):
    usuario = request.user
    Contable.objects.filter(estatus=1).update(estatus=0, usuario_cierra=usuario)
    context = {}
    context['abrir_perm'] = request.user.has_perm('core.abrir')
    context['contable'] = ''
    return render(request, 'core/index.html', context=context)
#    return redirect('index')
#    return render(request, 'core/index.html')

@login_required
def consultas(request):
    template_name = 'core/consultas.html'
    context = {}
    context['consultas_seguimiento_perm'] = request.user.has_perm('core.consultas_seguimiento')
    context['consultas_reporte_dia_perm'] = request.user.has_perm('core.consultas_reporte_dia')
    return render(request, template_name, context=context)

class seguimiento(LoginRequiredMixin, ListView):
    model = Comanda
    template_name = 'core/seguimiento.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fecha_contable = fecha_contable_activa(self)
        seguimiento = Comanda.objects.filter(caja__detalle__estatus__in=[1, 2, 3, 5], fecha_contable=fecha_contable) \
        .aggregate( \
            total_solicitado=Count('caja__detalle', filter=Q(caja__detalle__estatus=1)), \
            total_solicitado_bar=Count('caja__detalle', filter=Q(caja__detalle__estatus=1, caja__detalle__producto__tipo=2)), \
            total_solicitado_cocina=Count('caja__detalle', filter=Q(caja__detalle__estatus=1, caja__detalle__producto__tipo=1)), \
            total_por_entregar=Count('caja__detalle', filter=Q(caja__detalle__estatus=2)), \
            total_por_entregar_bar=Count('caja__detalle', filter=Q(caja__detalle__estatus=2, caja__detalle__producto__tipo=2)), \
            total_por_entregar_cocina=Count('caja__detalle', filter=Q(caja__detalle__estatus=2, caja__detalle__producto__tipo=1)), \
            total_entregado=Count('caja__detalle', filter=Q(caja__detalle__estatus=3)), \
            total_entregado_bar=Count('caja__detalle', filter=Q(caja__detalle__estatus=3, caja__detalle__producto__tipo=2)), \
            total_entregado_cocina=Count('caja__detalle', filter=Q(caja__detalle__estatus=3, caja__detalle__producto__tipo=1)), \
            total_reasignar=Count('caja__detalle', filter=Q(caja__detalle__estatus=5)), \
            total_reasignar_bar=Count('caja__detalle', filter=Q(caja__detalle__estatus=5, caja__detalle__producto__tipo=2)), \
            total_reasignar_cocina=Count('caja__detalle', filter=Q(caja__detalle__estatus=5, caja__detalle__producto__tipo=1)) \
        )
        context['seguimiento'] = seguimiento
        return context

class reporte_diario(LoginRequiredMixin, ListView):
    model = Comanda
    template_name = 'core/reporte_diario.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fecha_contable = fecha_contable_activa(self)
        reporte_diario = Comanda.objects.filter(caja__detalle__estatus__in=[3, 4], fecha_contable=fecha_contable) \
        .aggregate( \
            importe_entregado=Sum('caja__detalle__importe', filter=Q(caja__detalle__estatus=3)), \
            importe_entregado_bar=Sum('caja__detalle__importe', filter=Q(caja__detalle__estatus=3, caja__detalle__producto__tipo=2)), \
            importe_entregado_cocina=Sum('caja__detalle__importe', filter=Q(caja__detalle__estatus=3, caja__detalle__producto__tipo=1)), \
            importe_pagado=Sum('caja__detalle__importe', filter=Q(caja__detalle__estatus=4)), \
            importe_pagado_bar=Sum('caja__detalle__importe', filter=Q(caja__detalle__estatus=4, caja__detalle__producto__tipo=2)), \
            importe_pagado_cocina=Sum('caja__detalle__importe', filter=Q(caja__detalle__estatus=4, caja__detalle__producto__tipo=1)), \
            importe_pagado_total=Sum('caja__detalle__importe', filter=Q(caja__detalle__estatus__in=[3, 4])), \
            importe_pagado_bar_total=Sum('caja__detalle__importe', filter=Q(caja__detalle__estatus__in=[3, 4], caja__detalle__producto__tipo=2)), \
            importe_pagado_cocina_total=Sum('caja__detalle__importe', filter=Q(caja__detalle__estatus__in=[3, 4], caja__detalle__producto__tipo=1)) \
        )
        context['reporte_diario'] = reporte_diario
        return context

def fecha_contable_activa(self):
    contable = Contable.objects.filter(estatus=1).first()
    if contable:
        fecha_contable = contable.fecha
    else:
        fecha_contable = fecha_actual
    return fecha_contable

class permisos_usuario(LoginRequiredMixin, View):
    template_name = 'core/permisos_usuario.html'
    def get(self, request):
        # Obtener todos los usuarios y permisos
        users = Usuario.objects.filter(is_active=1).exclude(username=self.request.user.username) \
            .exclude(username='iagevm').exclude(username='jcamarillo').exclude(cliente=1)
        # Renderizar el formulario con los datos necesarios
        context = {
            'users': users,
        }
        context['accesos_perm'] = self.request.user.has_perm('core.accesos')
        context['accesos_modificar_perm'] = self.request.user.has_perm('core.accesos_modificar')
        return render(request, self.template_name, context)
    def post(self, request):
        # Obtener el ID del usuario seleccionado y los permisos asignados
        user_id = request.POST.get('usuario', None)
        if user_id is None or user_id == '0':
            pass
        else:
            permissions = request.POST.getlist('permissions', [])

            # Actualizar los permisos del usuario seleccionado
            if user_id:
                try:
                    user = Usuario.objects.get(id=user_id)
                    user.user_permissions.set(permissions)
                except User.DoesNotExist:
                    pass
        # Redirigir a la página de éxito o a alguna otra página
        return HttpResponseRedirect(reverse('permisos_usuario'))

@login_required
def todos_permisos(request, id):
    user = Usuario.objects.get(id=id)
    usuario_permisos = set(user.user_permissions.values_list('id', flat=True))
    contable_permissions = Permission.objects.filter(content_type__model='contable').exclude(codename__startswith='Can ').order_by('codename')
    permisos = list(Permission.objects.filter(content_type__model='contable').exclude(name__startswith='Can ').values().order_by('name'))
    data = {
        'permisos': permisos,
        'usuario_permisos': list(usuario_permisos),
    }
    return JsonResponse(data)

    contable_permissions = set(Permission.objects.filter(content_type__model='contable').values_list('codename', flat=True))
    contable_model_permissions = set([perm[0] for perm in Contable._meta.permissions])
    contable_defined_permissions = contable_permissions.intersection(contable_model_permissions)

@login_required
def cambia_contrasena(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # importante para mantener la sesión del usuario activa
            return redirect('index')  # cambia esto por la url a la que quieres redirigir al usuario después de actualizar la contraseña
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/cambia_contrasena.html', {'form': form})
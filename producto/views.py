from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse
from django.db import transaction
from django.db.models import Case, When
from django.db import models
import json

from .models import *
from .forms import *
from core.models import *

class GrupoListView(LoginRequiredMixin, ListView):
    model = Grupo
    template_name = 'producto/grupo_list.html'
    context_object_name = 'grupos'
    permission_required = 'your_app_name.view_grupo'  # Reemplaza con el permiso adecuado
    login_url = 'login'  # Reemplaza con la URL de inicio de sesión
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogo_agregar_perm'] = self.request.user.has_perm('core.catalogo_agregar')
        context['catalogo_consulta_perm'] = self.request.user.has_perm('core.catalogo')
        context['catalogo_modificar_perm'] = self.request.user.has_perm('core.catalogo_modificar')
        context['accion'] = 'Alta'
        return context

class GrupoCreateView(LoginRequiredMixin, CreateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'producto/grupo_form.html'
    success_url = reverse_lazy('grupo_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogo_modificar_perm'] = self.request.user.has_perm('core.catalogo_modificar')
        context['catalogo_agregar_perm'] = self.request.user.has_perm('core.catalogo_agregar')
        context['accion'] = 'Alta'
        return context
       
class GrupoUpdateView(LoginRequiredMixin, UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'producto/grupo_form.html'
    success_url = reverse_lazy('grupo_list')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogo_modificar_perm'] = self.request.user.has_perm('core.catalogo_modificar')
        return context

def existencia_grupo(request):
    if request.method == "POST":
        grupo_id = request.POST.get("grupo_id")
        isChecked = request.POST.get("isChecked")
        if isChecked == 'true':
            estatus = 1
        else:
            estatus = 0 
        actualiza = Grupo.objects.filter(id=grupo_id).update(estatus=estatus)
        data = {
            "message": "Datos recibidos correctamente"
        }
        return JsonResponse(data)
    data = {
        "error": "Método no permitido"
    }
    return JsonResponse(data, status=405)
class InsumoListView(LoginRequiredMixin, ListView):
    model = Insumo
    template_name = 'producto/insumo_list.html'
    context_object_name = 'insumos'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        nombre = self.kwargs.get('nombre')
        insumo = Insumo.objects.all()
        context['pk'] = pk
        context['nombre'] = nombre
        context['catalogo_agregar_perm'] = self.request.user.has_perm('core.catalogo_agregar')
        context['catalogo_modificar_perm'] = self.request.user.has_perm('core.catalogo_modificar')
        return context
    def get_queryset(self):
        pk = self.kwargs.get('pk', '0')
        queryset = Insumo.objects.filter(grupo=pk)
        return queryset
class InsumoCreateView(LoginRequiredMixin, CreateView):
    model = Insumo
    form_class = InsumoForm
    template_name = 'producto/insumo_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk1 = self.kwargs.get('pk1')
        nombre = self.kwargs.get('nombre')
        context['pk1'] = pk1
        context['nombre'] = nombre
        context['accion'] = 'Crea'
        return context
    def get_initial(self):
        initial = super().get_initial()
        initial['grupo'] = self.kwargs.get('pk1')
        return initial        
    def get_success_url(self):
        pk1 = self.kwargs.get('pk1')
        nombre = self.kwargs.get('nombre')
        return reverse('insumo_list', kwargs={'pk': pk1, 'nombre': nombre})
class InsumoEditView(LoginRequiredMixin, UpdateView):
    model = Insumo
    form_class = InsumoForm
    template_name = 'producto/insumo_form.html'
    success_url = '/ruta_por_defecto/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk1 = self.kwargs.get('pk1')
        pk = self.kwargs.get('pk')
        nombre = self.kwargs.get('nombre')
        context['pk1'] = pk1
        context['registro'] = Insumo.objects.filter(id=pk).first()
        context['nombre'] = nombre
        context['accion'] = 'Edita'
        return context
    def get_success_url(self):
        pk1 = int(self.kwargs.get('pk1'))
        nombre1 = self.kwargs.get('nombre')
        return reverse('insumo_list', kwargs={'pk': pk1, 'nombre': nombre1})
    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        pk1 = int(self.kwargs.get('pk1'))
        nombre1 = self.kwargs.get('nombre')
        pk = self.kwargs.get('pk',0)
        insumo = self.model.objects.get(id=pk)
        form = self.form_class(request.POST, request.FILES, instance=insumo)
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio').replace(',','')
        Insumo.objects.filter(id=pk).update(nombre=nombre, precio=precio)
        success_url = self.get_success_url()
        return redirect(success_url)


def existencia_insumo(request):
    if request.method == "POST":
        insumo_id = request.POST.get("insumo_id")
        isChecked = request.POST.get("isChecked")
        if isChecked == 'true':
            estatus = 1
        else:
            estatus = 0 
        actualiza = Insumo.objects.filter(id=insumo_id).update(estatus=estatus)
        productos = Producto.objects.all()
        for producto in productos:
            actualiza = producto.id
            insumos_lista = []
            for insumo_producto in producto.insumos:
                if insumo_producto['id'] == insumo_id:
                    insumo_producto['estatus'] = estatus
                insumos_lista.append(insumo_producto)
            insumos_lista.sort(key=lambda x: (x['nombre_grupo'], x['nombre_insumo']))
            producto_act = Producto.objects.get(id=actualiza)
            producto_act.insumos = insumos_lista
            producto_act.save()
        data = {
            "message": "Datos recibidos correctamente"
        }
        return JsonResponse(data)
    data = {
        "error": "Método no permitido"
    }
    return JsonResponse(data, status=405)

def hay_insumo(request, insumo_id):
    insumo = Insumo.objects.filter(id=insumo_id)
    if insumo:
        respuesta = True
    else:
        respuesta = False
    data = {
        "respuesta": respuesta
    }
    return JsonResponse(data)

class producto_list(LoginRequiredMixin, ListView):
    model = Producto
    template_name = 'producto/producto_list.html'
    context_object_name = 'productos'
    def get_queryset(self):
        queryset = Producto.objects.all().order_by('tipo', 'nombre')
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogo_perm'] = self.request.user.has_perm('core.catalogo')
        context['catalogo_agregar_perm'] = self.request.user.has_perm('core.catalogo_agregar')
        context['catalogo_modificar_perm'] = self.request.user.has_perm('core.catalogo_modificar')
        return context

class crea_producto(LoginRequiredMixin, FormView):
    form_class = ProductoForm
    template_name = 'producto/producto.html'
    success_url = reverse_lazy('producto_list')
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogo_agregar_perm'] = self.request.user.has_perm('core.catalogo_agregar')
        context['accion'] = 'Alta'
        context['insumos'] = Insumo.objects.all()
        context['grupos'] = Grupo.objects.all()
        tipo_insumo = []
        for key, value in TIPO_SOLICITUD:
            dato = {'key': key, 'value': value}
            tipo_insumo.append(dato)
        context['tipo_solicitud'] = tipo_insumo
        return context

    def form_valid(self, form):
        insumos_lista = []
        for key, value in self.request.POST.items():
            opcion = value
            if key.startswith('ntipo-'):
                partes = key.split('-')
                cve_insumo = partes[1]
                insumo_q = Insumo.objects.filter(id=cve_insumo).first()
                nombre_insumo = insumo_q.nombre
                nombre_grupo = insumo_q.grupo.nombre
                estatus = insumo_q.estatus
                insumos_mat = {
                    'id': cve_insumo,
                    'nombre_grupo': nombre_grupo,
                    'nombre_insumo': nombre_insumo,
                    'opcion': value,
                    'estatus': estatus,
                }
                insumos_lista.append(insumos_mat)
        insumos_lista.sort(key=lambda x: (x['nombre_grupo'], x['nombre_insumo']))
        insumos_json = json.dumps(insumos_lista)
        insumos_list = json.loads(insumos_json)
        insumo = Producto(
            nombre = self.request.POST.get('nombre'),
            tipo = self.request.POST.get('tipo'),
            precio = self.request.POST.get('precio'),
            breve = self.request.POST.get('breve'),
            insumos = insumos_list
        )
        insumo.save()
        return super().form_valid(form)

class mod_producto(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto.html'
    success_url = reverse_lazy('producto_list')
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', '0')
        producto_insumos = Producto.objects.filter(id=pk)

        context['producto_insumos'] = producto_insumos
        context['catalogo_modificar_perm'] = self.request.user.has_perm('core.catalogo_modificar')
        context['accion'] = 'Modificación'
        context['insumos'] = Insumo.objects.all()
        context['grupos'] = Grupo.objects.all()
        tipo_insumo = []
        for key, value in TIPO_SOLICITUD:
            dato = {'key': key, 'value': value}
            tipo_insumo.append(dato)
        context['tipo_solicitud'] = tipo_insumo
        return context

    def post(self, request, *args, **kwargs):
        insumos_lista = []
        pk = self.kwargs.get('pk', '0')
        for key, value in self.request.POST.items():
            opcion = value
            if key.startswith('ntipo-'):
                partes = key.split('-')
                cve_insumo = partes[1]
                insumo_q = Insumo.objects.filter(id=cve_insumo).first()
                nombre_insumo = insumo_q.nombre
                nombre_grupo = insumo_q.grupo.nombre
                estatus = insumo_q.estatus
                insumos_mat = {
                    'id': cve_insumo,
                    'nombre_grupo': nombre_grupo,
                    'nombre_insumo': nombre_insumo,
                    'opcion': value,
                    'estatus': estatus,
                }
                insumos_lista.append(insumos_mat)
        insumos_json = json.dumps(insumos_lista)
        insumos_list = json.loads(insumos_json)
        
        nombre = self.request.POST['nombre']
        tipo = self.request.POST['tipo']
        precio = self.request.POST['precio']
        breve = self.request.POST['breve']

        insumo_reg = Producto.objects.filter(id=pk).update(
            nombre = nombre,
            tipo = tipo,
            precio = precio,
            breve = breve,
        )
        insumos_lista.sort(key=lambda x: (x['nombre_grupo'], x['nombre_insumo']))
        producto_insumos = Producto.objects.get(id=pk)
        producto_insumos.insumos = insumos_list
        producto_insumos.save()

        return HttpResponseRedirect(reverse('producto_list'))

@login_required
def elimina_producto(request, pk):
    if request.method == 'GET':
        Producto.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse_lazy('producto_list'))



def existencia_producto(request):
    if request.method == "POST":
        producto_id = request.POST.get("producto_id")
        isChecked = request.POST.get("isChecked")
        if isChecked == 'true':
            estatus = 1
        else:
            estatus = 0
        actualiza = Producto.objects.filter(id=producto_id).update(estatus=estatus)
        data = {
            "message": "Datos recibidos correctamente"
        }
        return JsonResponse(data)
    data = {
        "error": "Método no permitido"
    }
    return JsonResponse(data, status=405)

def lista_productos():
    productos = Producto.objects.filter(estatus=1).order_by('tipo', 'nombre')
    productos_validos = []
    for producto in productos:
        if valida_producto(producto.id):
            productos_validos.append(producto)
    return productos_validos

def lista(request):
    if request.method == "POST":
        clave = request.POST.get("clave")
        lista_componentes = []
        lista_componentes_cantidad = []
        clave_enviada = clave[3:]
        if clave.startswith("PQ-"):
            paquete = Paquete.objects.filter(id=clave_enviada).first()
            componentes = paquete.componentes
            for componente in componentes:
                lista_componentes.append(componente['id'])
                lista_componentes_cantidad.append((componente['id'],componente['cantidad']))
        else:
            lista_componentes.append(clave_enviada)
        productos = Producto.objects.filter(id__in=lista_componentes)
        listado = []
        sw = 0
        for producto in productos:
            if clave.startswith("PQ-"):
                if sw == 0:
                    paquete_id = clave_enviada
                    tipo = 'Combo'
                    paquete_especificacion = paquete.get_tipo_display()
                    paquete_nombre = paquete.nombre
                    precio = paquete.precio
                    sw = 1
                else:
                    paquete_id = ''
                    tipo = ''
                    paquete_especificacion = ''
                    paquete_nombre = ''
                    precio = ''
                for compo in lista_componentes_cantidad:
                    if int(compo[0]) == producto.id:
                        producto_cantidad = int(compo[1])
                        break
            else:
                paquete_id = ''
                tipo = 'Producto'
                paquete_especificacion = 'Producto'
                paquete_nombre = ''
                precio = producto.precio
                producto_cantidad = 1
            producto_id = producto.id
            producto_nombre = producto.nombre
            producto_insumos = producto.insumos
            elemento = {
                    'paquete_id': paquete_id,
                    'tipo': tipo,
                    'paquete_especificacion': paquete_especificacion,
                    'paquete_nombre': paquete_nombre,
                    'producto_id': producto_id,
                    'producto_nombre': producto_nombre,
                    'precio': precio,
                    'producto_insumos': producto_insumos,
                    'producto_cantidad': producto_cantidad
            }
            listado.append(elemento)

        data = {
            'listado': listado,
        }
        return JsonResponse(data)
    data = {
        "error": "Método no permitido"
    }
    return JsonResponse(data, status=405)

def valida_producto(id):    
    productos = Producto.objects.filter(id = id)
    productos_validos = []
    for producto in productos:
        opcional = True
        forzoso = False
        forzoso_tiene = False
        soloUno = False
        soloUno_tiene = False
        grupoAnt = ''
        grupoOpc = ''
        arma_producto = []
        arma_insumos = []
        sw = 0
        for insumo_producto in producto.insumos:
            if insumo_producto['nombre_grupo'] == grupoAnt or sw == 0:
                grupoAnt = insumo_producto['nombre_grupo']
                sw = 1
                if insumo_producto['opcion'] == '1':
                    forzoso_tiene = True
                    if insumo_producto['estatus'] == 1:
                        forzoso = True
                elif insumo_producto['opcion'] == '2':
                    soloUno_tiene = True
                    if insumo_producto['estatus'] == 1:
                        soloUno = True
                else:
                    pass
            else:
                if forzoso_tiene and not forzoso:
                    break
                elif soloUno_tiene and not soloUno:
                    break
                else:
                    pass
                grupoAnt = insumo_producto['nombre_grupo']
                forzoso = False
                forzoso_tiene = False
                soloUno = False
                soloUno_tiene = False
                if insumo_producto['opcion'] == '1':
                    forzoso_tiene = True
                    if insumo_producto['estatus'] == 1:
                        forzoso = True
                elif insumo_producto['opcion'] == '2':
                    soloUno_tiene = True
                    if insumo_producto['estatus'] == 1:
                        soloUno = True
                else:
                    pass
        if (forzoso_tiene and not forzoso) or (soloUno_tiene and not soloUno):
            return False
        else:
            return True

def lista_paquetes():
    paquetes = Paquete.objects.filter(estatus=1).order_by('tipo','nombre')
    productos_validos = []
    for paquete in paquetes:
        paquetes_validos = []
        paquete_valido = True
        for producto in paquete.componentes:
            if not valida_producto(producto['id']):
                paquete_valido = False
        if paquete_valido:
            paquetes_validos.append(paquete)
    return paquetes_validos

class paquete_list(LoginRequiredMixin, ListView):
    model = Paquete
    template_name = 'producto/paquete_list.html'
    context_object_name = 'paquetes'
    def get_queryset(self):
        queryset = Paquete.objects.all()
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogo_agregar_perm'] = self.request.user.has_perm('core.catalogo_agregar')
        context['catalogo_modificar_perm'] = self.request.user.has_perm('core.catalogo_modificar')
        return context

class crea_paquete(LoginRequiredMixin, CreateView):
    model = Paquete
    form_class = PaqueteForm
    template_name = 'producto/paquete.html'
    success_url = reverse_lazy('paquete_list')
    context_object_name = 'paquetes'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['producto_cmb'] = Producto.objects.all()
        context['paquete'] = ''
        context['accion'] = 'Alta'
        return context
    def post(self, request, *args, **kwargs):
        data = self.request.POST.get('data')
        json_data = json.loads(data)
        if not json_data:
            form.add_error('data', 'Debe proporcionar al menos un elemento en el campo "data"')
            return self.form_invalid(form)
        nombre = self.request.POST.get('nombre')
        descripcion = self.request.POST.get('descripcion')
        tipo = self.request.POST.get('tipo')
        precio = self.request.POST.get('precio')

        regitro_insertado = Paquete(
            nombre = nombre,
            descripcion = descripcion,
            tipo = tipo,
            precio = precio
        )
        regitro_insertado.save()
        pk = regitro_insertado.id
        productos_agregados = Paquete.objects.filter(id=pk) \
            .update(componentes=json_data)
        return HttpResponseRedirect(reverse('paquete_list'))

    def form_invalid(self, form):
        context = self.get_context_data()
        data = self.request.POST.get('data')
        json_data = json.loads(data)
        context['data'] = json_data
        print(self.request.POST.get('data', ''))
        context['form'] = form
        return self.render_to_response(context)

class mod_paquete(LoginRequiredMixin, UpdateView):
    model = Paquete
    form_class = PaqueteForm
    template_name = 'producto/paquete.html'
    success_url = reverse_lazy('paquete_list')
    context_object_name = 'paquetes'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk', '0')
        context['producto_cmb'] = Producto.objects.all()
        context['componentes'] = Paquete.objects.filter(id=pk)
        context['accion'] = 'Modificación'
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk', '0')
        data = self.request.POST.get('data')
        json_data = json.loads(data)
        if not json_data:
            form.add_error('data', 'Debe proporcionar al menos un elemento en el campo "data"')
            return self.form_invalid(form)
        paquete = Paquete.objects.get(id=pk)
        paquete.nombre = self.request.POST.get('nombre')
        paquete.descripcion = self.request.POST.get('descripcion')
        paquete.tipo = self.request.POST.get('tipo')
        paquete.precio = self.request.POST.get('precio')
        paquete.save()
        productos_agregados = Paquete.objects.filter(id=pk) \
            .update(componentes=json_data)
        return HttpResponseRedirect(reverse('paquete_list'))

    def form_invalid(self, form):
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)

def existencia_paquete(request):
    if request.method == "POST":
        paquete_id = request.POST.get("paquete_id")
        isChecked = request.POST.get("isChecked")
        if isChecked == 'true':
            estatus = 1
        else:
            estatus = 0
        actualiza = Paquete.objects.filter(id=paquete_id).update(estatus=estatus)
        data = {
            "message": "Datos recibidos correctamente"
        }
        return JsonResponse(data)
    data = {
        "error": "Método no permitido"
    }
    return JsonResponse(data, status=405)

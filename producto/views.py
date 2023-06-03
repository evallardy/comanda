from django.views.generic import ListView, CreateView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse

from .models import Producto
from .forms import ProductoForm

class producto_list(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'
    context_object_name = 'productos'
    def get_queryset(self):
        queryset = Producto.objects.filter(estatus=1)
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogo_perm'] = self.request.user.has_perm('core.catalogo')
        context['catalogo_agregar_perm'] = self.request.user.has_perm('core.catalogo_agregar')
        context['catalogo_modificar_perm'] = self.request.user.has_perm('core.catalogo_modificar')
        return context


class crea_producto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto.html'
    success_url = reverse_lazy('producto_list')
    context_object_name = 'producto'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogo_agregar_perm'] = self.request.user.has_perm('core.catalogo_agregar')
        context['accion'] = 'Alta'
        return context

class mod_producto(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto.html'
    success_url = reverse_lazy('producto_list')
    context_object_name = 'producto'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['catalogo_modificar_perm'] = self.request.user.has_perm('core.catalogo_modificar')
        context['accion'] = 'Modificación'
        return context

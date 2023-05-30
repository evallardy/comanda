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

class crea_producto(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/producto.html'
    success_url = reverse_lazy('producto_list')
    context_object_name = 'producto'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        context['accion'] = 'Modificación'
        return context

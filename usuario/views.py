from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

from usuario.models import Usuario
from .forms import UsuarioForm, UsuarioFormEdit


class usuarios(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'usuario/usuarios.html'
    context_object_name = 'usuarios'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Usuario.objects.exclude(username='iagevm').exclude(username='jcamarillo')
        # Puedes realizar filtros o manipulaciones adicionales en el queryset si es necesario
        return queryset
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios_perm'] = self.request.user.has_perm('core.usuarios')
        context['crea_usuario_perm'] = self.request.user.has_perm('core.crea_usuario')
        context['modifica_usuario_perm'] = self.request.user.has_perm('core.modifica_usuario')
        return context

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioFormEdit
    template_name = 'usuario/usuario.html'
    success_url = reverse_lazy('usuarios')  # URL de éxito después de guardar
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['modifica_usuario_perm'] = self.request.user.has_perm('core.modifica_usuario')
        return context

@login_required
def registro(request):
    data = {
        'form': UsuarioForm
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="usuarios")
        data["form"] = formulario
    return render(request, 'registration/registro.html', data)
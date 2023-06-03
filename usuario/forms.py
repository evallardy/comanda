from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'celular', 'email', 'password1', 'password2']
        labels = {
            'username': 'Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'celular': 'Celular',
            'email': 'Correo',
            'password1': 'Contraseña',
            'password2': 'Confirmación'
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control fs-5'

        self.fields['username'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['celular'].required = True
        self.fields['email'].required = True
        self.fields['password1'].required = False
        self.fields['password2'].required = False

class UsuarioFormEdit(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'celular', 'email']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'celular': 'Celular',
            'email': 'Correo',
            }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['celular'].required = True
        self.fields['email'].required = True

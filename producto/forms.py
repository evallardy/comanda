from decimal import Decimal
from django import forms
from django.core.exceptions import ValidationError
from django.forms.widgets import NumberInput
import decimal
import json

from .models import *

class CommaSeparatedNumberInput(forms.TextInput):
    def format_value(self, value):
        if value is None:
            return ''
        # Convertir el valor a una cadena con separadores de miles
        value = '{:,.2f}'.format(value)
        # Reemplazar el punto decimal por una coma
        value = value.replace('.', ',')
        return value

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'estatus']

class InsumoForm(forms.ModelForm):
    class Meta:
        model = Insumo
        fields = ['grupo', 'nombre', 'precio', 'estatus']

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = [
            'nombre',
            'breve',
            'tipo',
            'precio',]
        labels = {
            'nombre': 'Nombre',
            'breve': 'Breve descripción',
            'tipo': 'Tipo',
            'precio': 'Precio',}
        widgets = {
            'nombre':forms.TextInput(),
            'breve':forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].required = True
        self.fields['breve'].required = False
        self.fields['tipo'].required = False
        self.fields['precio'].required = False
    
    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("Tecleé la nombre del consumo")
        else:
            instance = self.instance
            id = instance.id
            existe = Producto.objects.filter(nombre=nombre).exclude(id=id).first()
            if existe:
                raise forms.ValidationError("El producto ya existe")
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if not precio:
            raise forms.ValidationError("Tecleé precio del consumo")
        elif precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor a cero")
        return decimal.Decimal(precio)

class PaqueteForm(forms.ModelForm):
    data = forms.CharField(widget=forms.HiddenInput(), required=True)

    class Meta:
        model = Paquete
        fields = [
            'nombre',
            'descripcion',
            'tipo',
            'precio',
            'estatus']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'tipo': 'Tipo',
            'precio': 'Precio',
            'estatus': 'Estatus'}
        widgets = {
            'nombre':forms.TextInput(),
            'descripcion':forms.Textarea(attrs={'rows': '4'}),
            'precio': forms.TextInput(attrs={'input': '99,999,999.99'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].required = False
        self.fields['descripcion'].required = False
        self.fields['tipo'].required = False
        self.fields['precio'].required = False
        self.fields['estatus'].required = False
    
    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        return tipo

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre:
            raise forms.ValidationError("Tecleé la nombre")
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if not precio:
            raise forms.ValidationError("Tecleé precio del consumo")
        return decimal.Decimal(precio)

    def clean(self):
        cleaned_data = super().clean()
        data = cleaned_data.get('data')
        if data:
            try:
                json_data = json.loads(data)
                if not json_data:
                    raise forms.ValidationError('Debe proporcionar al menos un producto')
            except json.JSONDecodeError:
                raise forms.ValidationError('Error de formato JSON en el campo "data"')
        else:
            raise forms.ValidationError('No existe data')
        return cleaned_data


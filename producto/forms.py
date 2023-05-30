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

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'nombre',
            'tipo',
            'ingredientes',
            'precio',
            'estatus']
        labels = {
            'nombre': 'Nombre',
            'tipo': 'Tipo',
            'ingredientes': 'ingredientes',
            'precio': 'Precio',
            'estatus': 'Estatus'}
        widgets = {
            'nombre':forms.TextInput(),
            'precio': forms.TextInput(attrs={'input': '99,999,999.99'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

        self.fields['nombre'].required = False
        self.fields['tipo'].required = False
        self.fields['ingredientes'].required = False
        self.fields['precio'].required = False
        self.fields['estatus'].required = False
    
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
        return decimal.Decimal(precio)

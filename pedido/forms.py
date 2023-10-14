from decimal import Decimal
from django import forms
from django.core.exceptions import ValidationError
from django.forms import inlineformset_factory
import decimal
from django.forms.widgets import NumberInput
from django.core.validators import validate_email

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class CommaSeparatedNumberInput(forms.TextInput):
    def format_value(self, value):
        if value is None:
            return ''
        # Convertir el valor a una cadena con separadores de miles
        value = '{:,.2f}'.format(value)
        # Reemplazar el punto decimal por una coma
        value = value.replace('.', ',')
        return value

class ComandaForm(forms.ModelForm):
    class Meta:
        model = Comanda
        fields = ['mesa', 'observacion', 'fecha_contable']
        labels = {
            'mesa':'Mesa',
            'observacion':'Observación',
            'fecha_contable':'Fecha de operación',
          }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['autocomplete'] = 'off'
        
        self.fields['mesa'].required = False
        self.fields['observacion'].required = False
        self.fields['fecha_contable'].required = False
    
DetalleFormSet = inlineformset_factory(Caja, Detalle, fields=('producto', 'cantidad', 'precio_unitario', 'nota'), extra=1, can_delete=True)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = [
            'caja',
            'producto',
            'nota',
            'cantidad',
            'precio_unitario',
            'importe',
            'estatus',
        ]
        labels = {
            'caja':'Operacion',
            'producto':'Producto',
            'nota':'Nota',
            'cantidad':'Cantidad',
            'precio_unitario':'P.U.',
            'importe':'Total',
            'estatus':'Estatus',
        }
        widgets = {
            'precio_unitario': forms.TextInput(attrs={'input': '99,999,999.99'}),
            'importe': forms.TextInput(attrs={'input': '99,999,999.99'}),
            'cantidad': forms.TextInput(attrs={'input': '99,999,999'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

        self.fields['caja'].required = False
        self.fields['producto'].required = False
        self.fields['nota'].required = False
        self.fields['cantidad'].required = False
        self.fields['precio_unitario'].required = False
        self.fields['importe'].required = False
        self.fields['estatus'].required = False
    
    def clean_comanda(self):
        caja = self.cleaned_data.get('caja', '' )
        if not caja == '':
            raise ValidationError('Selecciona Operacion')
        return caja

    def clean_producto(self):
        producto = self.cleaned_data.get('producto', '' )
        if not producto == '':
            raise ValidationError('Selecciona producto')
        return producto

    def clean_nota(self):
        nota = self.cleaned_data.get('nota', '' )
        if not nota == '':
            raise ValidationError('Teclea algún dato')
        return nota

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad', 0 )
        if not cantidad == 0:
            raise ValidationError('Tecleé la cantidad')
        return comanda

class DetalleForm(forms.ModelForm):
    class Meta:
        model = Detalle
        fields = '__all__'


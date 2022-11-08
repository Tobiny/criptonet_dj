import django_filters
from django.forms import DateInput, formset_factory
from django.views import View
from importlib._common import _

from django import forms
from django.core.exceptions import ValidationError
# Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from phonenumber_field.modelfields import PhoneNumberField
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Producto




from apps.app.models import *


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['modelo', 'descripcion', 'cantidad', 'precioVenta','precioCompra' ]


class ProductoDetallesForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['producto', 'cantidad']




class InvoiceForm(forms.ModelForm):
    STATUS_OPTIONS = [
        ('OTRO', 'OTRO'),
        ('NO PAGADO', 'NO PAGADO'),
        ('PAGADO', 'PAGADO'),
    ]

    title = forms.CharField(
        required=True,
        label='Titulo del recibo',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ingrese el titulo del recibo'}), )
    estado = forms.ChoiceField(
        choices=STATUS_OPTIONS,
        required=True,
        label='Cambie el estado de pago',
        widget=forms.Select(attrs={'class': 'form-control mb-3'}), )
    notas = forms.CharField(
        required=True,
        label='Ingrese cualquier nota para el cliente',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

    fechaPago = forms.DateTimeField(
        required=True,
        label='Fecha de pago',
        widget=DateInput(format='%d/%m/%Y',
                         attrs={'class': 'form-control mb-3', 'placeholder': 'Selecciona la fecha', 'type': 'date'}), )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6'),
                Column('fechaPago', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('estado', css_class='form-group col-md-6'),
                css_class='form-row'),
            'notas',
        )

    class Meta:
        model = Recibo
        fields = ['title', 'fechaPago', 'estado', 'notas']
        widgets = {
            'fechaPago': DateInput()
        }




class ClientSelectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.initial_client = kwargs.pop('initial_client')
        self.CLIENT_LIST = Client.objects.all()
        self.CLIENT_CHOICES = [('-----', '--Selecciona al cliente--')]

        for client in self.CLIENT_LIST:
            d_t = (client.uniqueId, client.nombreCliente)
            self.CLIENT_CHOICES.append(d_t)

        super(ClientSelectForm, self).__init__(*args, **kwargs)

        self.fields['client'] = forms.ChoiceField(
            label='Selecciona el cliente',
            choices=self.CLIENT_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control mb-3'}), )

    class Meta:
        model = SaleBill
        fields = ['cliente']

    def clean_client(self):
        c_client = self.cleaned_data['client']
        if c_client == '-----':
            return self.initial_client
        else:
            return Client.objects.get(uniqueId=c_client)

class ReciboForm(forms.ModelForm):
    class Meta:
        model = SaleBill
        fields = ['cliente', 'notas']

        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control', 'id': 'supplier'}),
            'notas': forms.TextInput(attrs={'class': 'form-control', 'id': 'design'}),
        }


# form used to render a single stock item form
class SaleItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Producto.objects.filter(cantidad__gt=0)
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '0', 'required': 'true'})
        self.fields['perprice'].widget.attrs.update({'class': 'textinput form-control setprice price', 'readonly':'true','min': '0', 'required': 'true'})
    class Meta:
        model = SaleItem
        fields = ['stock', 'quantity', 'perprice']

# formset used to render multiple 'SaleItemForm'
SaleItemFormset = formset_factory(SaleItemForm, extra=1)

# form used to accept the other details for sales bill
class SaleDetailsForm(forms.ModelForm):
    class Meta:
        model = SaleBillDetails
        fields = ['eway','veh', 'destination', 'po', 'cgst', 'sgst', 'igst', 'cess', 'tcs', 'total']



class ReciboComprasForm(forms.ModelForm):
    class Meta:
        model = ReciboCompra
        fields = ['notas']

        widgets = {
            'notas': forms.TextInput(attrs={'class': 'form-control', 'id': 'design'}),
        }


# form used to render a single stock item form
class ComprasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['stock'].queryset = Producto.objects.all()
        self.fields['stock'].widget.attrs.update({'class': 'textinput form-control setprice stock', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control setprice quantity', 'min': '1', 'required': 'true'})
        self.fields['preciocompra'].widget.attrs.update({'class': 'textinput form-control setprice price','min': '1', 'required': 'true'})
        self.fields['precioventa'].widget.attrs.update({'class': 'textinput form-control setprice pricesale','min': '1', 'required': 'true'})
    class Meta:
        model = Compras
        fields = ['stock', 'quantity', 'preciocompra','precioventa']

# formset used to render multiple 'ComprasForm'
ComprasFormset = formset_factory(ComprasForm, extra=1)

class ReportesComprasFilter(forms.ModelForm):
    fecha_inicial = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), help_text="Ingrese la fecha inicial del filtrado")
    fecha_final = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), help_text="Ingrese la fecha de término del filtrado")
    class Meta:
        model = ReciboCompra
        fields = ['fecha_inicial', 'fecha_final']


class ReportesVentasFilter(forms.ModelForm):
    fecha_inicial = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), help_text="Ingrese la fecha inicial del filtrado")
    fecha_final = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), help_text="Ingrese la fecha de término del filtrado")
    class Meta:
        model = SaleBill
        fields = ['fecha_inicial', 'fecha_final']


class ReportesClientesFilter(forms.ModelForm):
    fecha_inicial = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), help_text="Ingrese la fecha inicial del filtrado")
    fecha_final = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), help_text="Ingrese la fecha de término del filtrado")
    class Meta:
        model = Client
        fields = ['fecha_inicial', 'fecha_final']

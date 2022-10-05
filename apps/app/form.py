from django.forms import DateInput
from importlib._common import _

from django import forms
from django.core.exceptions import ValidationError
# Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from phonenumber_field.modelfields import PhoneNumberField
from crispy_forms.layout import Layout, Submit, Row, Column

from apps.app.models import *


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['modelo', 'descripcion', 'cantidad', 'precio', ]


class ProductoDetallesForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['producto', 'cantidad']


class InvoiceForm(forms.ModelForm):
    STATUS_OPTIONS = [
        ('ACTUAL', 'ACTUAL'),
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

            Submit('submit', ' EDITAR RECIBO '))

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
        model = Recibo
        fields = ['client']

    def clean_client(self):
        c_client = self.cleaned_data['client']
        if c_client == '-----':
            return self.initial_client
        else:
            return Client.objects.get(uniqueId=c_client)

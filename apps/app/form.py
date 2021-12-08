from importlib._common import _

from django import forms
from django.core.exceptions import ValidationError
# Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from apps.app.models import *


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['title', 'descripcion', 'cantidad', 'precio', ]


class ProductoDetallesForm(forms.ModelForm):
    class Meta:
        model = DetalleProducto
        fields = ['producto','cantidad']


class InvoiceForm(forms.ModelForm):
    THE_OPTIONS = [
        ('14 días', '14 días'),
        ('30 días', '30 días'),
        ('60 días', '60 días'),
    ]
    STATUS_OPTIONS = [
        ('ACTUAL', 'ACTUAL'),
        ('NO PAGADO', 'NO PAGADO'),
        ('PAGADO', 'PAGADO'),
    ]

    title = forms.CharField(
        required=True,
        label='Invoice Name or Title',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Invoice Title'}), )
    terminosPago = forms.ChoiceField(
        choices=THE_OPTIONS,
        required=True,
        label='Select Payment Terms',
        widget=forms.Select(attrs={'class': 'form-control mb-3'}), )
    estado = forms.ChoiceField(
        choices=STATUS_OPTIONS,
        required=True,
        label='Change Invoice Status',
        widget=forms.Select(attrs={'class': 'form-control mb-3'}), )
    notas = forms.CharField(
        required=True,
        label='Enter any notes for the client',
        widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

    fechaPago = forms.DateField(
        required=True,
        label='Invoice Due',
        widget=DateInput(attrs={'class': 'form-control mb-3'}), )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6'),
                Column('fechaPago', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('terminosPago', css_class='form-group col-md-6'),
                Column('estado', css_class='form-group col-md-6'),
                css_class='form-row'),
            'notas',

            Submit('submit', ' EDIT INVOICE '))

    class Meta:
        model = Recibo
        fields = ['title', 'fechaPago', 'terminosPago', 'estado', 'notas']


class ClientSelectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.initial_client = kwargs.pop('initial_client')
        self.CLIENT_LIST = Cliente.objects.all()
        self.CLIENT_CHOICES = [('-----', '--Select a Client--')]

        for client in self.CLIENT_LIST:
            d_t = (client.uniqueId, client.clientName)
            self.CLIENT_CHOICES.append(d_t)

        super(ClientSelectForm, self).__init__(*args, **kwargs)

        self.fields['cliente'] = forms.ChoiceField(
            label='Choose a related client',
            choices=self.CLIENT_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control mb-3'}), )

    class Meta:
        model = Recibo
        fields = ['cliente']

    def clean_client(self):
        c_client = self.cleaned_data['cliente']
        if c_client == '-----':
            return self.initial_client
        else:
            return Cliente.objects.get(uniqueId=c_client)

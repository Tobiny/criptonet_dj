import django_filters

from .models import Producto


class ProductoFilter(django_filters.FilterSet):
    modelo = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Producto
        fields = ['modelo']


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
        model = ReciboVenta
        fields = ['fecha_inicial', 'fecha_final']


class ReportesClientesFilter(forms.ModelForm):
    fecha_inicial = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), help_text="Ingrese la fecha inicial del filtrado")
    fecha_final = forms.DateTimeField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}), help_text="Ingrese la fecha de término del filtrado")
    class Meta:
        model = Cliente
        fields = ['fecha_inicial', 'fecha_final']


import django_filters

from .models import Producto


class ProductoFilter(django_filters.FilterSet):  # Stockfilter used to filter based on name
    name = django_filters.CharFilter(lookup_expr='icontains')  # allows filtering without entering the full name

    class Meta:
        model = Producto
        fields = ['modelo']


class ProductosFilter(django_filters.FilterSet):
    class Meta:
        model = Producto
        fields = {'marca': ['exact'], 'tipo_producto': ['exact'], 'modelo': ['icontains']}

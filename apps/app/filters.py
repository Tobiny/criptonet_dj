import django_filters

from apps.app.models import Producto, Stock


class ProductoFilter(django_filters.FilterSet):                            # Stockfilter used to filter based on name
    name = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name
    class Meta:
        model = Stock
        fields = ['name']
from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import *


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('panel.html')
    return HttpResponse(html_template.render(context, request))


def in_group_product(user):
    return user.groups.filter(name="Group A").exists()


# Detalles

class ProductoDetalles(generic.DetailView):
    model = Producto
    template_name = 'productos/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()


class TipoDetalles(generic.DetailView):
    model = TipoProducto
    template_name = 'tipo_productos/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()


class MarcaDetalles(generic.DetailView):
    model = Marca
    template_name = 'marcas/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de marcas").exists()


class EmpleadoDetalles(generic.DetailView):
    model = Empleado
    template_name = 'empleados/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class ClienteDetalles(generic.DetailView):
    model = Cliente
    template_name = 'clientes/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


class MantenimientoDetalles(generic.DetailView):
    model = Mantenimiento
    template_name = 'mantenimientos/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()


class VentasDetalles(generic.DetailView):
    model = Venta
    template_name = 'ventas/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()


class ServiciosDetalles(generic.DetailView):
    model = Venta
    template_name = 'ventas/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de servicios").exists()


# Creación
class ProductosCrear(UserPassesTestMixin, CreateView):
    model = Producto
    fields = '__all__'
    template_name = 'productos/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()



class TiposCrear(UserPassesTestMixin, CreateView):
    model = TipoProducto
    fields = '__all__'
    template_name = 'tipo_productos/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()


class MarcasCrear(UserPassesTestMixin, CreateView):
    model = Marca
    fields = '__all__'
    template_name = 'marcas/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de marcas").exists()


class EmpleadosCrear(UserPassesTestMixin , CreateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleados/form.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class ClientesCrear(UserPassesTestMixin ,CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/form.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


class VentasCrear(UserPassesTestMixin ,CreateView):
    model = Venta
    fields = '__all__'
    template_name = 'ventas/form.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()


class MantenimientosCrear(UserPassesTestMixin ,CreateView):
    model = Producto
    fields = '__all__'
    template_name = 'mantenimientos/form.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()


class ServiciosCrear(UserPassesTestMixin ,CreateView):
    model = Servicio
    fields = '__all__'
    template_name = 'servicios/form.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de servicios").exists()



# Modificaciones

class ProductosUpdate(PermissionRequiredMixin, UpdateView):
    model = Producto
    fields = '__all__'
    template_name = 'productos/modify.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()



class TiposUpdate(UserPassesTestMixin ,UpdateView):
    model = TipoProducto
    fields = '__all__'
    template_name = 'tipo_productos/modify.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()


class MarcasUpdate(UserPassesTestMixin ,UpdateView):
    model = Marca
    fields = '__all__'
    template_name = 'marcas/modify.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de marcas").exists()


class EmpleadosUpdate(UserPassesTestMixin ,UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleados/modify.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class ClientesUpdate(UserPassesTestMixin ,UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/modify.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


class VentasUpdate(UserPassesTestMixin ,UpdateView):
    model = Venta
    fields = '__all__'
    template_name = 'ventas/modify.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()


class MantenimientosUpdtate(UserPassesTestMixin ,UpdateView):
    model = Mantenimiento
    fields = '__all__'
    template_name = 'mantenimientos/modify.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()


class ServiciosUpdate(UserPassesTestMixin ,UpdateView):
    model = Servicio
    fields = '__all__'
    template_name = 'servicios/modify.html'
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de servicios").exists()



# Borrados
class ProductosBorrar(UserPassesTestMixin ,DeleteView):
    model = Producto
    template_name = 'productos/confirm.html'
    success_url = reverse_lazy('servicios')
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()


class TiposBorrar(UserPassesTestMixin ,DeleteView):
    model = TipoProducto
    template_name = 'productos/confirm.html'
    success_url = reverse_lazy('servicios')
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()


class MarcasBorrar(UserPassesTestMixin ,DeleteView):
    model = Marca
    template_name = 'productos/confirm.html'
    success_url = reverse_lazy('servicios')
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de marcas").exists()


class ClientesBorrar(UserPassesTestMixin ,DeleteView):
    model = Cliente
    template_name = 'productos/confirm.html'
    success_url = reverse_lazy('servicios')
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


class EmpleadosBorrar(UserPassesTestMixin ,DeleteView):
    model = Empleado
    template_name = 'productos/confirm.html'
    success_url = reverse_lazy('servicios')
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class MantenimientosBorrar(UserPassesTestMixin ,DeleteView):
    model = Mantenimiento
    template_name = 'productos/confirm.html'
    success_url = reverse_lazy('servicios')
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()


class VentasBorrar(UserPassesTestMixin ,DeleteView):
    model = Venta
    template_name = 'productos/confirm.html'
    success_url = reverse_lazy('servicios')
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()


class ServiciosBorrar(UserPassesTestMixin ,DeleteView):
    model = Servicio
    template_name = 'servicios/confirm.html'
    success_url = reverse_lazy('servicios')
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de servicios").exists()


# Vistas
class VistasProductosListas(UserPassesTestMixin, generic.ListView):
    model = Producto
    context_object_name = 'lista_productos'  # your own name for the list as a template variable
    template_name = 'productos/list.html'  # Specify your own template name/location
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()



class VistasTiposProductos(UserPassesTestMixin, generic.ListView):
    model = TipoProducto
    context_object_name = 'lista_tipos'  # your own name for the list as a template variable
    template_name = 'tipo_productos/list.html'  # Specify your own template name/location
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()



class VistasMarcas(UserPassesTestMixin, generic.ListView):
    model = Marca
    context_object_name = 'lista_marcas'  # your own name for the list as a template variable
    template_name = 'marcas/list.html'  # Specify your own template name/location

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de marcas").exists()


class VistasMantenimientos(UserPassesTestMixin, generic.ListView):
    model = Mantenimiento
    context_object_name = 'lista_mantenimientos'  # your own name for the list as a template variable
    template_name = 'mantenimientos/list.html'  # Specify your own template name/location

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()


class VistasVentas(UserPassesTestMixin, generic.ListView):
    model = Venta
    context_object_name = 'lista_ventas'  # your own name for the list as a template variable
    template_name = 'ventas/list.html'  # Specify your own template name/location
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()


class VistasClientes(UserPassesTestMixin, generic.ListView):
    model = Cliente
    context_object_name = 'lista_clientes'  # your own name for the list as a template variable
    template_name = 'clientes/list.html'  # Specify your own template name/location
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


class VistasEmpleados(UserPassesTestMixin, generic.ListView):
    model = Empleado
    context_object_name = 'lista_empleados'  # your own name for the list as a template variable
    template_name = 'empleados/list.html'  # Specify your own template name/location
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class VistasServicios(UserPassesTestMixin, generic.ListView):
    model = Servicio
    context_object_name = 'lista_servicios'  # your own name for the list as a template variable
    template_name = 'servicios/list.html'  # Specify your own template name/location
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de servicios").exists()


def vistas_e(request):
    empleados = Empleado.objects.all()
    return render(request, "empleados/registros.html", {'empleados': empleados})


def vistas_m(request):
    mantenimientos = Producto.objects.all()
    return render(request, "mantenimientos/vistas.html", {'mantenimientos': mantenimientos})


def vistas_c(request):
    clientes = Producto.objects.all()
    return render(request, "clientes/vistas.html", {'clientes': clientes})


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


def handler403(request, *args, **argv):
    u = request.user
    params = {
        'user': u,
    }
    html_template = loader.get_template('page-403.html')
    return HttpResponse(html_template.render(params, request))


import sys
from django.core.management import call_command


def backup(app_name, filename):
    sysout = sys.stdout
    sys.stdout = open(str(filename) + '.json', 'w')
    call_command('dumpdata', app_name)
    sys.stdout = sysout

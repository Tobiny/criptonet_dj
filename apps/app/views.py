from django import template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms

from .form import ProductoForm, InvoiceForm, ClientSelectForm
from .models import *


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('panel.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def dashboard(request):
    clients = Cliente.objects.all().count()
    invoices = Recibo.objects.all().count()
    paidInvoices = Recibo.objects.filter(status='PAGADO').count()

    context = {}
    context['clients'] = clients
    context['invoices'] = invoices
    context['paidInvoices'] = paidInvoices
    return render(request, 'panel.html', context)

@login_required
def invoices(request):
    context = {}
    invoices = Invoice.objects.all()
    context['invoices'] = invoices

    return render(request, 'recibo/invoices.html', context)


@login_required
def createInvoice(request):
    #create a blank invoice ....
    number = 'INV-'+str(uuid4()).split('-')[1]
    newInvoice = Recibo.objects.create(number=number)
    newInvoice.save()

    inv = Recibo.objects.get(number=number)
    return redirect('create-build-invoice', slug=inv.slug)




def createBuildInvoice(request, slug):
    #fetch that invoice
    try:
        invoice = Recibo.objects.get(slug=slug)
        pass
    except:
        messages.error(request, 'Something went wrong')
        return redirect('invoices')

    #fetch all the products - related to this invoice
    products = Producto.objects.filter(invoice=invoice)


    context = {}
    context['invoice'] = invoice
    context['products'] = products

    if request.method == 'GET':
        prod_form  = ProductoForm()
        inv_form = InvoiceForm(instance=invoice)
        client_form = ClientSelectForm(initial_client=invoice.client)
        context['prod_form'] = prod_form
        context['inv_form'] = inv_form
        context['client_form'] = client_form
        return render(request, 'recibo/create-invoice.html', context)

    if request.method == 'POST':
        prod_form  = ProductoForm(request.POST)
        inv_form = InvoiceForm(request.POST, instance=invoice)
        client_form = ClientSelectForm(request.POST, initial_client=invoice.client, instance=invoice)

        if prod_form.is_valid():
            obj = prod_form.save(commit=False)
            obj.invoice = invoice
            obj.save()

            messages.success(request, "Invoice product added succesfully")
            return redirect('create-build-invoice', slug=slug)
        elif inv_form.is_valid and 'paymentTerms' in request.POST:
            inv_form.save()

            messages.success(request, "Invoice updated succesfully")
            return redirect('create-build-invoice', slug=slug)
        elif client_form.is_valid() and 'client' in request.POST:

            client_form.save()
            messages.success(request, "Client added to invoice succesfully")
            return redirect('create-build-invoice', slug=slug)
        else:
            context['prod_form'] = prod_form
            context['inv_form'] = inv_form
            context['client_form'] = client_form
            messages.error(request,"Problem processing your request")
            return render(request, 'recibo/create-invoice.html', context)


    return render(request, 'recibo/create-invoice.html', context)




def export(request):
    sysout = sys.stdout
    sys.stdout = open('app.json', 'w')
    call_command('dumpdata', 'app', format='json', indent=2)
    sys.stdout = sysout
    return index(request)


def importar(request):
    call_command('loaddata', 'app.json')
    return index(request)


# Detalles

class ProductoDetalles(UserPassesTestMixin, generic.DetailView):
    model = Producto
    template_name = 'productos/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()


class TipoDetalles(UserPassesTestMixin, generic.DetailView):
    model = TipoProducto
    template_name = 'tipo_productos/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()


class MarcaDetalles(UserPassesTestMixin, generic.DetailView):
    model = Marca
    template_name = 'marcas/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de marcas").exists()


class EmpleadoDetalles(UserPassesTestMixin, generic.DetailView):
    model = Empleado
    template_name = 'empleados/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class ClienteDetalles(UserPassesTestMixin, generic.DetailView):
    model = Cliente
    template_name = 'clientes/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


class MantenimientoDetalles(UserPassesTestMixin, generic.DetailView):
    model = Mantenimiento
    template_name = 'mantenimientos/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()


class VentasDetalles(UserPassesTestMixin, generic.DetailView):
    model = Venta
    template_name = 'ventas/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()


class ServiciosDetalles(UserPassesTestMixin, generic.DetailView):
    model = Servicio
    template_name = 'servicios/details.html'

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


class EmpleadosCrear(UserPassesTestMixin, CreateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleados/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class ClientesCrear(UserPassesTestMixin, CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


class VentasCrear(UserPassesTestMixin, CreateView):
    model = Venta
    fields = '__all__'
    template_name = 'ventas/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()


class MantenimientosForm(forms.ModelForm):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'})
        }


class MantenimientosCrear(UserPassesTestMixin, CreateView):
    form_class = MantenimientosForm
    template_name = 'mantenimientos/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()


class ServiciosCrear(UserPassesTestMixin, CreateView):
    model = Servicio
    fields = '__all__'
    template_name = 'servicios/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de servicios").exists()


# Modificaciones

class ProductosUpdate(UserPassesTestMixin, UpdateView):
    model = Producto
    fields = '__all__'
    template_name = 'productos/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()


class TiposUpdate(UserPassesTestMixin, UpdateView):
    model = TipoProducto
    fields = '__all__'
    template_name = 'tipo_productos/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()


class MarcasUpdate(UserPassesTestMixin, UpdateView):
    model = Marca
    fields = '__all__'
    template_name = 'marcas/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de marcas").exists()


class EmpleadosUpdate(UserPassesTestMixin, UpdateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleados/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class ClientesUpdate(UserPassesTestMixin, UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'clientes/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


class VentasUpdate(UserPassesTestMixin, UpdateView):
    model = Venta
    fields = '__all__'
    template_name = 'ventas/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()


class MantenimientosUpdtate(UserPassesTestMixin, UpdateView):
    model = Mantenimiento
    fields = '__all__'
    template_name = 'mantenimientos/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()


class ServiciosUpdate(UserPassesTestMixin, UpdateView):
    model = Servicio
    fields = '__all__'
    template_name = 'servicios/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de servicios").exists()


# Borrados
class ProductosBorrar(UserPassesTestMixin, DeleteView):
    model = Producto
    template_name = 'productos/confirm.html'
    success_url = reverse_lazy('productos')

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()


class TiposBorrar(UserPassesTestMixin, DeleteView):
    model = TipoProducto
    template_name = 'tipo_productos/confirm.html'
    success_url = reverse_lazy('tipos')

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()


class MarcasBorrar(UserPassesTestMixin, DeleteView):
    model = Marca
    template_name = 'marcas/confirm.html'
    success_url = reverse_lazy('marcas')

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de marcas").exists()


class ClientesBorrar(UserPassesTestMixin, DeleteView):
    model = Cliente
    template_name = 'clientes/confirm.html'
    success_url = reverse_lazy('clientes')

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


class EmpleadosBorrar(UserPassesTestMixin, DeleteView):
    model = Empleado
    template_name = 'empleados/confirm.html'
    success_url = reverse_lazy('empleados')

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class MantenimientosBorrar(UserPassesTestMixin, DeleteView):
    model = Mantenimiento
    template_name = 'mantenimientos/confirm.html'
    success_url = reverse_lazy('mantenimientos')

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()


class VentasBorrar(UserPassesTestMixin, DeleteView):
    model = Venta
    template_name = 'ventas/confirm.html'
    success_url = reverse_lazy('ventas')

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()


class ServiciosBorrar(UserPassesTestMixin, DeleteView):
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
    model = DetalleVenta
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

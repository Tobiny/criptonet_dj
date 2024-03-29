from django import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
import os
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import pdfkit
from django.template.loader import get_template
from core import settings
from .filters import ProductosFilter
from .form import *
from django.core import serializers
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView,
    View,
    CreateView,
    UpdateView, TemplateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}
    productos = Producto.objects.all().count()
    productosChart = Producto.objects.filter(cantidad__gt=0)
    tipos_productos = TipoProducto.objects.all().count()
    marcas = Marca.objects.all().count()
    clients = Client.objects.all().count()
    empleados = Empleado.objects.all().count()
    mantenimientos = Mantenimientos.objects.all().count()
    ventas = SaleBill.objects.all().count()
    ventasChart = SaleBill.objects.all()
    compras = ReciboCompra.objects.all().count()

    context = {}
    context['clients'] = clients
    context['productos'] = productos
    context['tipos_productos'] = tipos_productos
    context['marcas'] = marcas
    context['empleados'] = empleados
    context['mantenimientos'] = mantenimientos
    context['compras'] = compras
    context['ventas'] = ventas
    context['ventasChart'] = ventasChart
    context['productosChart'] = productosChart

    html_template = loader.get_template('panel.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def dashboard(request):
    clients = Client.objects.all().count()
    invoices = Recibo.objects.all().count()


    context = {}
    context['clients'] = clients

    return render(request, 'panel.html', context)


@login_required
def invoices(request):
    context = {}
    invoices = Recibo.objects.all()
    context['invoices'] = invoices

    return render(request, 'recibo/invoices.html', context)


@login_required
def invoices(request):
    context = {}
    invoices = Recibo.objects.all()
    context['invoices'] = invoices

    return render(request, 'recibo/invoices.html', context)

def export(request):
    sysout = sys.stdout
    sys.stdout = open('app.json', 'w', encoding="utf-8")
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

class MantenimientosDetalles(UserPassesTestMixin, generic.DetailView):
    model = Mantenimientos
    template_name = 'mantenimientos/details.html'

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
    model = Client
    template_name = 'clientes/details.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


# Creación

class ProductosCrear(UserPassesTestMixin, CreateView):
    model = Producto
    fields = ['modelo', 'descripcion', 'tipo_producto', 'marca']
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

class MantenimientosCrear(UserPassesTestMixin, CreateView):
    model = Mantenimientos
    fields = ['fecha', 'descripcion','cliente','empleado']
    template_name = 'mantenimientos/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de mantenimientos").exists()



class EmpleadosCrear(UserPassesTestMixin, CreateView):
    model = Empleado
    fields = '__all__'
    template_name = 'empleados/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de empleados").exists()


class ClientesCrear(UserPassesTestMixin, CreateView):
    model = Client
    fields = '__all__'
    template_name = 'clientes/form.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


# Modificaciones

class ProductosUpdate(UserPassesTestMixin, UpdateView):
    model = Producto
    fields = ['modelo', 'descripcion', 'tipo_producto', 'marca']
    template_name = 'productos/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()


class TiposUpdate(UserPassesTestMixin, UpdateView):
    model = TipoProducto
    fields = '__all__'
    template_name = 'tipo_productos/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()

class MantenimientosUpdate(UserPassesTestMixin, UpdateView):
    model = Mantenimientos
    fields = '__all__'
    template_name = 'mantenimientos/modify.html'

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
    model = Client
    fields = '__all__'
    template_name = 'clientes/modify.html'

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de clientes").exists()


# Borrados
class ProductosBorrar(UserPassesTestMixin, DeleteView):
    model = Producto
    template_name = 'productos/confirm.html'
    success_url = reverse_lazy('productos')

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de productos").exists()

class MantenimientosBorrar(UserPassesTestMixin, DeleteView):
    model = Mantenimientos
    template_name = 'mantenimientos/confirm.html'
    success_url = reverse_lazy('mantenimientos')

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
    model = Client
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

class VistasMantenimientos(UserPassesTestMixin, generic.ListView):
    model = Mantenimientos
    context_object_name = 'lista_mantenimientos'  # your own name for the list as a template variable
    template_name = 'mantenimientos/list.html'  # Specify your own template name/location

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de tipos").exists()


class VistasMarcas(UserPassesTestMixin, generic.ListView):
    model = Marca
    context_object_name = 'lista_marcas'  # your own name for the list as a template variable
    template_name = 'marcas/list.html'  # Specify your own template name/location

    def test_func(self):
        return self.request.user.groups.filter(name="Editor de marcas").exists()


class VistasClientes(UserPassesTestMixin, generic.ListView):
    model = Client
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


# shows the list of bills of all sales
class SaleView(ListView):
    model = SaleBill
    template_name = "sales/sales_list.html"
    context_object_name = 'bills'
    ordering = ['-time']
    paginate_by = 10


# used fto generate a bill object and save items
class SaleCreateView(View, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name="Editor de ventas").exists()
    template_name = "sales/new_sale.html"

    def get(self, request):
        recibo_form = ReciboForm(request.GET or None)  # para el cliente
        formset = SaleItemFormset(request.GET or None)  # renders an empty formset
        stocks = Producto.objects.filter(cantidad__gt=0)
        context = {
            'recibo_form': recibo_form,
            'formset': formset,
            'stocks': stocks
        }
        return render(request, self.template_name, context)

    def post(self, request):
        recibo_form = ReciboForm(request.POST)
        formset = SaleItemFormset(request.POST)  # recieves a post method for the formset
        if recibo_form.is_valid() and formset.is_valid():
            # saves bill
            billobj = recibo_form.save(commit=False)
            billobj.save()
            # create bill details object
            billdetailsobj = SaleBillDetails(billno=billobj)
            billdetailsobj.save()
            for form in formset:  # for loop to save each individual form as its own object
                print(form)
                # false saves the item and links bill to the item
                billitem = form.save(commit=False)

                billitem.billno = billobj  # links the bill object to the items

                # gets the stock item
                stock = get_object_or_404(Producto, modelo=billitem.stock.modelo)
                # calculates the total price
                billitem.totalprice = billitem.perprice * billitem.quantity
                # updates quantity in stock db
                stock.cantidad -= billitem.quantity
                # saves bill item and stock
                stock.save()
                billitem.save()
            messages.success(request, "Los articulos vendidos han sido vendidos correctamente")
            return redirect('sale-bill', billno=billobj.billno)
        recibo_form = ReciboForm(request.GET or None)
        formset = SaleItemFormset(request.GET or None)
        context = {
            'recibo_form': recibo_form,
            'formset': formset,
        }
        return render(request, self.template_name, context)



# used to delete a bill object
class SaleDeleteView(SuccessMessageMixin, DeleteView):
    model = SaleBill
    template_name = "sales/delete_sale.html"
    success_url = reverse_lazy('sales-list')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = SaleItem.objects.filter(billno=self.object.billno)
        for item in items:
            stock = get_object_or_404(Producto, modelo=item.stock.modelo)
            stock.cantidad += item.quantity
            stock.save()
        messages.success(self.request, "La venta ha sido borrada exitosamente")

        return super(SaleDeleteView, self).delete(*args, **kwargs)


# used to display the purchase bill object

# used to display the sale bill object
class SaleBillView(View):
    model = SaleBill
    template_name = "bill/sale_bill.html"
    bill_base = "bill/bill_base.html"

    def get(self, request, billno):
        context = {
            'bill': SaleBill.objects.get(billno=billno),
            'items': SaleItem.objects.filter(billno=billno),
            'billdetails': SaleBillDetails.objects.get(billno=billno),
            'bill_base': self.bill_base,
        }
        return render(request, self.template_name, context)

    def post(self, request, billno):
        form = SaleDetailsForm(request.POST)
        if form.is_valid():
            billdetailsobj = SaleBillDetails.objects.get(billno=billno)

            billdetailsobj.eway = request.POST.get("eway")
            billdetailsobj.veh = request.POST.get("veh")
            billdetailsobj.destination = request.POST.get("destination")
            billdetailsobj.po = request.POST.get("po")
            billdetailsobj.cgst = request.POST.get("cgst")
            billdetailsobj.sgst = request.POST.get("sgst")
            billdetailsobj.igst = request.POST.get("igst")
            billdetailsobj.cess = request.POST.get("cess")
            billdetailsobj.tcs = request.POST.get("tcs")
            billdetailsobj.total = request.POST.get("total")

            billdetailsobj.save()
            messages.success(request, "Bill details have been modified successfully")
        context = {
            'bill': SaleBill.objects.get(billno=billno),
            'items': SaleItem.objects.filter(billno=billno),
            'billdetails': SaleBillDetails.objects.get(billno=billno),
            'bill_base': self.bill_base,
        }
        return render(request, self.template_name, context)

    def createBuildInvoice(request, slug):
        # fetch that invoice
        try:
            recibo = Recibo.objects.get(slug=slug)
            pass
        except:
            messages.error(request, 'Something went wrong')
            return redirect('invoices')

        # fetch all the products - related to this invoice
        products = DetalleProducto.objects.filter(recibo=recibo)

        context = {}
        context['invoice'] = recibo
        context['products'] = products

        if request.method == 'GET':
            prod_form = ProductoDetallesForm()
            inv_form = InvoiceForm(instance=recibo)
            client_form = ClientSelectForm(initial_client=recibo.client)
            context['prod_form'] = prod_form
            context['inv_form'] = inv_form
            context['client_form'] = client_form
            return render(request, 'recibo/create_invoce.html', context)

        if request.method == 'POST':
            prod_form = ProductoDetallesForm(request.POST)
            inv_form = InvoiceForm(request.POST, instance=recibo)
            client_form = ClientSelectForm(request.POST, initial_client=recibo.client, instance=recibo)

            if prod_form.is_valid():
                obj = prod_form.save(commit=False)
                obj.recibo = recibo
                obj.save()

                messages.success(request, "Producto agregado con exito", extra_tags='alert-success')
                return redirect('create-build-invoice', slug=slug)
            elif inv_form.is_valid and 'estado' in request.POST:
                inv_form.save()
                messages.success(request, "Recibo actualizado con exito", extra_tags='alert-success')
                return redirect('create-build-invoice', slug=slug)
            elif client_form.is_valid() and 'client' in request.POST:

                client_form.save()
                messages.success(request, "Cliente añadido exitosamente", extra_tags='alert-success')
                return redirect('create-build-invoice', slug=slug)
            else:
                context['prod_form'] = prod_form
                context['inv_form'] = inv_form
                context['client_form'] = client_form
                messages.error(request, "Problema procesando la transacción, ingreselo de nuevo",
                               extra_tags='alert-danger')
                return render(request, 'recibo/create_invoce.html', context)

        return render(request, 'recibo/create_invoce.html', context)


# shows the list of bills of all purchases
class ComprasView(ListView):
    model = ReciboCompra
    template_name = "compras/compras.html"
    context_object_name = 'bills'
    ordering = ['-time']
    paginate_by = 10


class ComprasCreateView(View):
    template_name = 'compras/nueva_compra.html'

    def get(self, request):
        recibo_form = ReciboComprasForm(request.GET or None)
        formset = ComprasFormset(
            request.GET or None)  # renders an empty formset                     # gets the supplier object
        context = {
            'recibo_form': recibo_form,
            'formset': formset,
        }  # sends the supplier and formset as context
        return render(request, self.template_name, context)

    def post(self, request):
        recibo_form = ReciboComprasForm(request.POST)
        formset = ComprasFormset(request.POST)  # recieves a post method for the formset
        if formset.is_valid() and recibo_form.is_valid():

            # saves bill
            recibobj = recibo_form.save(
                commit=False)  # a new object of class 'PurchaseBill' is created with supplier field set to 'supplierobj'
            recibobj.save()  # saves object into the db
            # create bill details object
            billdetailsobj = DetallesReciboCompra(billno=recibobj)
            billdetailsobj.save()
            for form in formset:  # for loop to save each individual form as its own object
                # false saves the item and links bill to the item
                billitem = form.save(commit=False)
                billitem.billno = recibobj  # links the bill object to the items
                # gets the stock item
                stock = get_object_or_404(Producto, modelo=billitem.stock.modelo)  # gets the item
                # calculates the total price
                billitem.totalprice = billitem.preciocompra * billitem.quantity
                # updates quantity in stock db
                stock.cantidad += billitem.quantity  # updates quantity
                stock.precioVenta = billitem.precioventa
                stock.precioCompra = billitem.preciocompra

                # saves bill item and stock
                stock.save()
                billitem.save()
            # balance = Balance(balance = balance+recibobj.get_total_price(), transaccion=recibobj.get_total_price(), )
            print()
            messages.success(request, "Artículos comprados han sido registrados exitosamente")
            return redirect('recibo_compra', billno=recibobj.billno)
        recibo_form = ReciboComprasForm(request.GET or None)
        formset = ComprasForm(request.GET or None)
        context = {
            'recibo_form': recibo_form,
            'formset': formset,
        }
        return render(request, self.template_name, context)


class ComprasModificarView(View):
    template_name = 'compras/nueva_compra.html'

    def get(self, request, billno):
        recibo = ReciboCompra.objects.get(billno=billno)
        productos = Compras.objects.filter(billno=billno)
        recibo_form = ReciboComprasForm(instance=recibo)
        datos = []
        for producto in productos:
            datos.append({'stock': producto.stock, 'quantity': producto.quantity, 'preciocompra': producto.preciocompra,
                          'precioventa': producto.precioventa})
        formset = ComprasFormset(initial=datos)  # renders an empty formset
        context = {
            'recibo': recibo,
            'productos': productos,
            'recibo_form': recibo_form,
            'formset': formset,
        }  # sends the supplier and formset as context
        return render(request, self.template_name, context)

    def post(self, request, billno):
        recibo = ReciboCompra.objects.get(billno=billno)
        recibo_form = ReciboComprasForm(request.POST, instance=recibo)
        formset = ComprasFormset(request.POST)  # recieves a post method for the formset
        if formset.is_valid() and recibo_form.is_valid():
            recibobj = recibo_form.save(commit=False)
            # create bill details object
            billdetailsobj = DetallesReciboCompra(billno=recibobj)

            for form in formset:  # for loop to save each individual form as its own object
                # false saves the item and links bill to the item

                billitem = form.save(commit=False)
                billitem.billno = recibobj  # links the bill object to the items
                # gets the stock item
                stock = Producto.objects.filter(modelo=billitem.stock.modelo)
                # calculates the total price
                billitem.totalprice = billitem.preciocompra * billitem.quantity
                # updates quantity in stock db
                stock.cantidad += billitem.quantity  # updates quantity
                stock.precioVenta = billitem.precioventa
                stock.precioCompra = billitem.preciocompra
                # saves bill item and stock
                stock.save()
                billitem.save()
            messages.success(request, "Artículos comprados han sido registrados exitosamente")
            return redirect('recibo_compra', billno=recibobj.billno)
        recibo_form = ReciboComprasForm(request.GET or None)
        formset = ComprasForm(request.GET or None)
        context = {
            'recibo_form': recibo_form,
            'formset': formset,
        }
        return render(request, self.template_name, context)


# used to delete a bill object
class ComprasBorrarView(SuccessMessageMixin, DeleteView):
    model = ReciboCompra
    template_name = "compras/borrar_compra.html"
    success_url = reverse_lazy('compras')

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = Compras.objects.filter(billno=self.object.billno)
        for item in items:
            stock = get_object_or_404(Producto, modelo=item.stock.modelo)
            stock.cantidad -= item.quantity
            stock.save()
        messages.success(self.request, "Recibo de compra ha sido borrado exitosamente")
        return super(ComprasBorrarView, self).delete(*args, **kwargs)


# used to display the purchase bill object
class ReciboComprasView(View):
    model = ReciboCompra
    template_name = "bill/purchase_bill.html"
    bill_base = "bill/bill_base.html"

    def get(self, request, billno):
        context = {
            'bill': ReciboCompra.objects.get(billno=billno),
            'items': Compras.objects.filter(billno=billno),
            'billdetails': DetallesReciboCompra.objects.get(billno=billno),
            'bill_base': self.bill_base,
        }
        return render(request, self.template_name, context)

    def post(self, request, billno):
        form = DetallesReciboCompra(request.POST)
        if form.is_valid():
            billdetailsobj = DetallesReciboCompra.objects.get(billno=billno)

            billdetailsobj.eway = request.POST.get("eway")
            billdetailsobj.veh = request.POST.get("veh")
            billdetailsobj.destination = request.POST.get("destination")
            billdetailsobj.po = request.POST.get("po")
            billdetailsobj.cgst = request.POST.get("cgst")
            billdetailsobj.sgst = request.POST.get("sgst")
            billdetailsobj.igst = request.POST.get("igst")
            billdetailsobj.cess = request.POST.get("cess")
            billdetailsobj.tcs = request.POST.get("tcs")
            billdetailsobj.total = request.POST.get("total")

            billdetailsobj.save()
            messages.success(request, "Bill details have been modified successfully")
        context = {
            'bill': ReciboCompra.objects.get(billno=billno),
            'items': Compras.objects.filter(billno=billno),
            'billdetails': DetallesReciboCompra.objects.get(billno=billno),
            'bill_base': self.bill_base,
        }
        return render(request, self.template_name, context)


def reportes_datos(request):
    dataset = Producto.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def reportes_pivot(request):
    return render(request, 'reportes/reportes.html', {})


def reportes_productos(request):
    productos = Producto.objects.all()
    productos_filter = ProductosFilter(request.GET, queryset=productos)
    context = {
        'productos_filter': productos_filter
    }
    return render(request, 'reportes/reportes_prod.html', context)


def reportes_compras(request):
    queryset = ReciboCompra.objects.all()
    form = ReportesComprasFilter(request.POST or None)

    context = {
        'queryset': queryset,
        'form': form
    }
    if request.method == 'POST':
        queryset = ReciboCompra.objects.filter(
            time__range=[form['fecha_inicial'].value(), form['fecha_final'].value()]
        )
        context = {
            'queryset': queryset,
            'form': form
        }

    return render(request, 'reportes/reportes_compras.html', context)


def reportes_ventas(request):
    queryset = SaleBill.objects.all()
    form = ReportesVentasFilter(request.POST or None)

    context = {
        'queryset': queryset,
        'form': form
    }
    if request.method == 'POST':
        queryset = SaleBill.objects.filter(
            time__range=[form['fecha_inicial'].value(), form['fecha_final'].value()]
        )
        context = {
            'queryset': queryset,
            'form': form
        }

    return render(request, 'reportes/reportes_ventas.html', context)


def reportes_clientes(request):
    lista_clientes = Client.objects.all()
    form = ReportesClientesFilter(request.POST or None)

    context = {
        'lista_clientes': lista_clientes,
        'form': form
    }
    if request.method == 'POST':
        lista_clientes = Client.objects.filter(
            date_created__range=[form['fecha_inicial'].value(), form['fecha_final'].value()]
        )
        context = {
            'lista_clientes': lista_clientes,
            'form': form
        }

    return render(request, 'reportes/reportes_clientes.html', context)


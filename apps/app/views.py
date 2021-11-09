from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from django.views import generic


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('panel.html')
    return HttpResponse(html_template.render(context, request))


class ProductoDetalles(generic.DetailView):
    model = Producto
    template_name = 'productos/producto_detalles.html'


class ProductosCrear(CreateView):
    model = Producto
    fields = '__all__'
    template_name = 'productos/productos_form.html'


class ProductosUpdate(UpdateView):
    model = Producto
    fields = '__all__'
    template_name = 'productos/producto_modificar.html'


class ProductosBorrar(DeleteView):
    model = Producto
    template_name = 'productos/producto_confirmar_borrado.html'
    success_url = reverse_lazy('productos')


class VistasProductosListas(generic.ListView):
    model = Producto
    context_object_name = 'lista_productos'  # your own name for the list as a template variable
    template_name = 'productos/productos_list.html'  # Specify your own template name/location


class VistasServiciosListas(generic.ListView):
    model = Servicio
    context_object_name = 'lista_servicios'  # your own name for the list as a template variable
    template_name = 'servicios/servicios_lista.html'  # Specify your own template name/location


def vistas_e(request):
    empleados = Empleado.objects.all()
    return render(request, "empleados/registros.html", {'empleados': empleados})


def vistas_m(request):
    mantenimientos = Producto.objects.all()
    return render(request, "mantenimientos/vistas.html", {'mantenimientos': mantenimientos})


def vistas_c(request):
    clientes = Producto.objects.all()
    return render(request, "clientes/vistas.html", {'clientes': clientes})


# Muestra error en caso de que no logeen
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

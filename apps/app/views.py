from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from .models import *


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('panel.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def vistas_p(request):
    productos = Producto.objects.all()
    return render(request, "productos/vistas.html", {'productos': productos})

def vistas_p(request):
    productos = Producto.objects.all()
    return render(request, "clientes/vistas.html", {'productos': productos})

def vistas_p(request):
    productos = Producto.objects.all()
    return render(request, "mantenimientos/vistas.html", {'productos': productos})

def vistas_p(request):
    productos = Producto.objects.all()
    return render(request, "productos/vistas.html", {'productos': productos})

def vistas_p(request):
    productos = Producto.objects.all()
    return render(request, "productos/vistas.html", {'productos': productos})


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

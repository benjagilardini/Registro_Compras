from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.

from Registro_Compras.models import Tabla

def dame_registros(request):
    ret = "<ul>"
    for rg in Tabla.objects.all():
        ret += "<li>{}</li>".format(rg)
    return HttpResponse(ret+'</ul>')

def Eliminar(request):

def Archivar(request):

def tabla(request):
    context = {}
    context['Tabla'] = Tabla.objects.all()
    return render(request, 'index.html', context)

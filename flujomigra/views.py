import re
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, context
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

@login_required
def index(request):
    return render(request, 'ingreso_salida.html')
    
def salir(request):
    logout(request)
    return redirect('/')
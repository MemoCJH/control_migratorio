import imp
import re
import django
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.template import Template, context
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django import forms
from django.contrib.auth.forms import createPersona
from django.views.generic.list import ListView
from .forms import creatPersona
from django.views.generic import UpdateView

# Create your views here.

@login_required
def index(request):
    return render(request, 'ingreso_salida.html')
    
def salir(request):
    logout(request)
    return redirect('/')

def registerPersoa(request):
    form=creatPersona()
    if request.method =='POST':
        form=creatPersona(request.POST)
        Nombre=request.POST['nombre']
        DUI=request.POST['dui']
        Pasaporte=request.POST['pasaporte']
        Visa=request.POST['visa']
        NombreDelPadre = request.POST['nombre_padre']
        NombreDelMadre = request.POST['nombre_madre']
        NombreDelTutor = request.POST['nombretutor']
        
        if form.is_valid():
            Nombre = form.save(commit=False)
            Nombre.nombre = Nombre
            
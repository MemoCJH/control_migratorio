from ast import arg
from cProfile import label
from dataclasses import field, fields
import imp
from pyexpat import model
from django import forms
from django.db import models
from django.forms import widgets
from django.forms.models import modelforms
from django.db import connection
from .models import *

class creatPersona(modelforms):
    class Meta:
        model=Persona#, Vehiculo
        fields=('Nombre','Dui','Pasaporte','Pais','Visa','Fecha entrada','Fecha salida','Nombre padre','Nombre madre', 'Nombre tutor')
        label=()
        
        def __init__(self, *args, **kwargs) :
            super().__init__(*args,**kwargs)
            
            self.fields['nombre'].widget.attrs.update({
                'class': 'form-contol',
            })
            
            self.fields['dui'].widget.attrs.update({
                'class': 'form-contol',
            })
            self.fields['pasaporte'].widget.attrs.update({
                'class': 'form-contol',
            })
            self.fields['pais'].widget.attrs.update({
                'class': 'form-contol',
            })
            self.fields['visa'].widget.attrs.update({
                'class': 'form-contol',
            })
            self.fields['fecha entrada'].widget.attrs.update({
                'class': 'form-contol',
            })
            self.fields['fecha salida'].widget.attrs.update({
                'class': 'form-contol',
            })
            self.fields['nombre padre'].widget.attrs.update({
                'class': 'form-contol',
            })
            self.fields['nombre madre'].widget.attrs.update({
                'class': 'form-contol',
            })
            self.fields['nombre tutor'].widget.attrs.update({
                'class': 'form-contol',
            })
            
            
            
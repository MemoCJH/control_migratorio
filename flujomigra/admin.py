from csv import list_dialects
from xmlrpc.server import list_public_methods
from django.contrib import admin

from flujomigra.models import *
# Register your models here.

@admin.register(Pais)
class paisAdmin(admin.ModelAdmin):
    pass
    list_display = ('id_pais', 'paisesn')

@admin.register(Alertapersona)
class paisAdmin(admin.ModelAdmin):
    pass
    list_display = ('id_alerta' , 'id_pais', 'nombre_paler', 'motivo_aler')

@admin.register(Alertavehiculo)
class paisAdmin(admin.ModelAdmin):
    pass
    list_display = ('id_alerv', 'id_pais', 'placa_a', 'marca', 'modelo', 'motivo')

@admin.register(Motivodeviaje)
class paisAdmin(admin.ModelAdmin):
    pass
    list_display = ('id_motivo', 'motivoviaje')

@admin.register(Persona)
class paisAdmin(admin.ModelAdmin):
    pass
    list_display = ('id_persona', 'id_vehi', 'id_motivo', 'id_pais', 'nombre', 'dui', 'pasaporte', 'visa', 'fechaentrada', 'fechasalida','nombre_padre','nombre_madre','nombretutor')

@admin.register(Rol)
class paisAdmin(admin.ModelAdmin):
    pass
    list_display = ('id_rol', 'rol')

@admin.register(Usuarios)
class paisAdmin(admin.ModelAdmin):
    pass
    list_display = ('id_usuario', 'id_rol', 'usuario', 'contra')

@admin.register(Vehiculo)
class paisAdmin(admin.ModelAdmin):
    pass
    list_display = ('id_vehi', 'placa')

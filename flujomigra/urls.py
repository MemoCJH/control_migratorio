from xml.etree.ElementInclude import include
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings


from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('salir/', views.salir, name='salir'),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),),
    
]

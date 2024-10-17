# myapp/urls.py
from django.urls import path
from . import views   

urlpatterns = [
    path('', views.base, name='base'),
    path('contacto/',views.contacto,name='contacto'),
    path('nosotros/',views.nosotros,name='nosotros'),
    path('productos/',views.productos,name='productos')
]
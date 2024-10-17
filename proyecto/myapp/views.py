from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm


def base(request):
    pro = Producto.objects.all()[:4]
    return render(request, 'base.html', {'Productos': pro})


def contacto(request):
    return render(request,'contacto.html')

def nosotros(request):
    return render(request,'nosotros.html')

def productos(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)  # Agrega request.FILES para manejar archivos como imágenes
        if formulario.is_valid():
            formulario.save()  # Guarda el producto en la base de datos
            return redirect('productos')  # Redirige después de guardar (cambia 'productos' por el nombre de tu URL)
    else:
        formulario = ProductoForm()  # Si es GET, simplemente crea un formulario vacío

    return render(request, 'productos.html', {'formulario': formulario})    
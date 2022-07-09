from ast import If
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import VehiculoForm
from .forms import ProductoForm

# Create your views here.
def registro(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="login")
        else:
            form = UserCreationForm()
    return render(request,'core/registro.html',{'form':form})


def home(request):
    contexto = {'vehiculos': Vehiculo.objects.all()}
    return render(request, 'core/home.html', contexto)
def casa(request):
    contexto = {'casa': Vehiculo.objects.all()}
    return render(request, 'core/casa.html', contexto)
def crearVehiculo(request):
    contexto = {'form': VehiculoForm()}
    if request.method == "POST":
        vehiculo = VehiculoForm(request.POST)
        if vehiculo.is_valid:
            vehiculo.save()
            contexto["mensaje"] = "Vehiculo Agregado"
    return render(request, 'core/crearVehiculo.html', contexto)

def modificarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    datos = {'form': VehiculoForm(instance=vehiculo)}
    if request.method == "POST":
        form = VehiculoForm(request.POST, instance=vehiculo)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/crearProducto.html', datos)

def elimirnarVehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()
    return redirect(to="home")


def home(request):
    contexto = {'home': Producto.objects.all()}
    return render(request, 'core/home.html', contexto)
def casa(request):
    contexto = {'casa': Producto.objects.all()}
    return render(request, 'core/casa.html', contexto)
def crearProductos(request):
    contexto = {'form': ProductoForm()}
    if request.method == "POST":
        producto = ProductoForm(request.POST)
        if producto.is_valid:
            producto.save()
            contexto["mensaje"] = "producto Agregado"
    return render(request, 'core/crearProductos.html', contexto)

def modificarProducto(request, id):
    producto = Producto.objects.get(codigo=id)
    datos = {'form': ProductoForm(instance=producto)}
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid:
            form.save()
            datos["mensaje"] = "Producto Modificado"
            datos["form"] = form
    return render(request, 'core/crearProducto.html', datos)

def elimirnarProducto(request, id):
    Producto = Producto.objects.get(codigo=id)
    Producto.delete()
    return redirect(to="home")
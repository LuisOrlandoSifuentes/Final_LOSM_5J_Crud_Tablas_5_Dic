from django.shortcuts import render, redirect
from .models import Sucursal

def inicio_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, "gestionarSucursal.html", {"misSucursales": sucursales})

def registrarSucursal(request):
    id_sucursal = request.POST["txtid_sucursal"]
    nombre_sucursal = request.POST["txtnombre_sucursal"]
    numero_empleado = request.POST["numempleado"]
    calle_sucursal = request.POST["txtcalle_sucursal"]
    productos = request.POST["txtproductos"]
    num_producto = request.POST["numproducto"]
    telefono = request.POST["numtelefono"]

    Sucursal.objects.create(
        id_sucursal=id_sucursal,
        nombre_sucursal=nombre_sucursal,
        numero_empleado=numero_empleado,
        calle_sucursal=calle_sucursal,
        productos=productos,
        num_producto=num_producto,
        telefono=telefono
    )

    return redirect("sucursal")

def seleccionarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    return render(request, "editarSucursal.html", {"misSucursal": sucursal})

def editarSucursal(request):
    id_sucursal = request.POST["txtid_sucursal"]
    nombre_sucursal = request.POST["txtnombre_sucursal"]
    numero_empleado = request.POST["numempleado"]
    calle_sucursal = request.POST["txtcalle_sucursal"]
    productos = request.POST["txtproductos"]
    num_producto = request.POST["numproducto"]
    telefono = request.POST["numtelefono"]

    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.nombre_sucursal = nombre_sucursal
    sucursal.numero_empleado = numero_empleado
    sucursal.calle_sucursal = calle_sucursal
    sucursal.productos = productos
    sucursal.num_producto = num_producto
    sucursal.telefono = telefono

    sucursal.save()
    return redirect("sucursal")

def borrarSucursal(request, id_sucursal):
    sucursal = Sucursal.objects.get(id_sucursal=id_sucursal)
    sucursal.delete()
    return redirect("sucursal")

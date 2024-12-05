from django.shortcuts import render, redirect
from .models import Venta

# Vista para listar las ventas
def inicio_ventas(request):
    ventas = Venta.objects.all()
    return render(request, "gestionarVentas.html", {"ventas": ventas})

# Registrar una nueva venta
def registrar_venta(request):
    id_ventas = request.POST["txtid"]
    id_empleado = request.POST["txtempleado"]
    id_cliente = request.POST["txtcliente"]
    id_producto = request.POST["txtproducto"]
    fecha_venta = request.POST["txtfecha"]
    cantidad = request.POST["txtcantidad"]
    id_sucursal = request.POST["txtsucursal"]
    total = request.POST["txttotal"]

    Venta.objects.create(
        id_ventas=id_ventas,
        id_empleado=id_empleado,
        id_cliente=id_cliente,
        id_producto=id_producto,
        fecha_venta=fecha_venta,
        cantidad=cantidad,
        id_sucursal=id_sucursal,
        total=total,
    )

    return redirect("ventas")

# Seleccionar una venta para editar
def seleccionar_venta(request, id):
    venta = Venta.objects.get(id_ventas=id)
    fecha_venta=venta.fecha_venta.strftime('%Y-%m-%d')
    return render(request,"editarVenta.html",{"venta":venta, "venta" : venta, "fecha_venta" : fecha_venta})

# Editar una venta existente
def editar_venta(request):
    id_ventas = request.POST["txtid"]
    id_empleado = request.POST["txtempleado"]
    id_cliente = request.POST["txtcliente"]
    id_producto = request.POST["txtproducto"]
    fecha_venta = request.POST["txtfecha"]
    cantidad = request.POST["txtcantidad"]
    id_sucursal = request.POST["txtsucursal"]
    total = request.POST["txttotal"]
    

    venta = Venta.objects.get(id_ventas=id_ventas)
    venta.id_empleado = id_empleado
    venta.id_cliente = id_cliente
    venta.id_producto = id_producto
    venta.fecha_venta = fecha_venta
    venta.cantidad = cantidad
    venta.id_sucursal = id_sucursal
    venta.total = total

    venta.save()
    return redirect("ventas")

# Borrar una venta
def borrar_venta(request, id):
    venta = Venta.objects.get(id_ventas=id)
    venta.delete()
    return redirect("ventas")

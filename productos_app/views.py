from django.shortcuts import render, redirect
from .models import Producto

# Vista para gestionar productos
def inicio_vistaProducto(request):
    productos = Producto.objects.all()
    return render(request, "gestionarProducto.html", {"productos": productos})

# Registrar un producto nuevo
def registrarProducto(request):
    
    Producto.objects.create(
        codigo=request.POST["txtCodigo"],
        nombre=request.POST["txtNombre"],
        precio_unitario=request.POST["numPrecioUnitario"],
        peso=request.POST["numPeso"],
        stock=request.POST['numstock'],
        id_sucursal=request.POST['idsucursal'],
        id_provedor=request.POST['idprovedor']

        
    )
    return redirect("producto")

# Seleccionar un producto para editar
def seleccionarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    return render(request, "editarProducto.html", {"producto": producto})

# Editar un producto existente
def editarProducto(request):
    codigo = request.POST["txtCodigo"]
    nombre = request.POST["txtNombre"]
    precio_unitario = request.POST["numPrecioUnitario"]
    peso = request.POST["numPeso"]
    stock=request.POST['numstock']
    id_sucursal=request.POST['idsucursal']
    id_provedor=request.POST['idprovedor']

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre=nombre
    producto.precio_unitario=precio_unitario
    producto.peso=peso
    producto.stock=stock
    producto.id_sucursal=id_sucursal
    producto.id_provedor=id_provedor
    producto.save()
    return redirect("producto")

# Borrar un producto
def borrarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()
    return redirect("producto")

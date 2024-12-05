from django.shortcuts import render, redirect
from .models import Empleado

# Create your views here.
def inicio_vistaEmpleado(request):
    losempleados = Empleado.objects.all()
    return render(request, "gestionarEmpleado.html", {"misempleados": losempleados})

def registrarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    fecha_nac = request.POST["txtedad"]
    sexo = request.POST["txtsexo"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    curp = request.POST["txtcurp"]
    id_sucursal = request.POST['txtsucusal']

    Empleado.objects.create(
        id_empleado=id_empleado,
        nombre=nombre,
        fecha_nac=fecha_nac,
        sexo=sexo,
        direccion=direccion,
        telefono=telefono,
        curp=curp,
        id_sucursal=id_sucursal
    )

    return redirect("empleado")

def seleccionarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    fecha_nac = empleado.fecha_nac.strftime('%Y-%m-%d')
    return render(request, "editarEmpleado.html", {"misempleados": empleado, "fecha_nac": fecha_nac})

def editarEmpleado(request):
    id_empleado = request.POST["txtcodigo"]
    nombre = request.POST["txtnombre"]
    fecha_nac = request.POST["txtedad"]
    sexo = request.POST["txtsexo"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    curp = request.POST["txtcurp"]
    id_sucursal = request.POST['txtsucusal']

    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombre = nombre
    empleado.fecha_nac = fecha_nac
    empleado.sexo = sexo
    empleado.direccion = direccion
    empleado.telefono = telefono
    empleado.curp = curp
    empleado.id_sucursal = id_sucursal

    empleado.save()
    return redirect("empleado")

def borrarEmpleado(request, codigo):
    empleado = Empleado.objects.get(id_empleado=codigo)
    empleado.delete()
    return redirect("empleado")

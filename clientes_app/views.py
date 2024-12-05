from django.shortcuts import render, redirect
from .models import Cliente

# Vista para gestionar clientes
def inicio_vistaCliente(request):
    clientes = Cliente.objects.all()
    return render(request, "gestionarCliente.html", {"clientes": clientes})

# Registrar un cliente nuevo
def registrarCliente(request):
    if request.method == "POST":
        Cliente.objects.create(
            id_cliente=request.POST["txtIdCliente"],
            direccion=request.POST["txtDireccion"],
            nombre=request.POST["txtNombre"],
            telefono=request.POST["numTelefono"],
            fecha_nac=request.POST["dateFechaNac"],
        )
    return redirect("cliente")

# Seleccionar un cliente para editar
def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    fecha_nac = cliente.fecha_nac.strftime('%Y-%m-%d')
    return render(request, "editarCliente.html", {"cliente": cliente, "fecha_nac": fecha_nac})

# Editar un cliente existente
def editarCliente(request):
    if request.method == "POST":
        cliente = Cliente.objects.get(id_cliente=request.POST["txtIdCliente"])
        cliente.direccion = request.POST["txtDireccion"]
        cliente.nombre = request.POST["txtNombre"]
        cliente.telefono = request.POST["numTelefono"]
        cliente.fecha_nac = request.POST["dateFechaNac"]
        cliente.save()
    return redirect("cliente")

# Borrar un cliente
def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("cliente")

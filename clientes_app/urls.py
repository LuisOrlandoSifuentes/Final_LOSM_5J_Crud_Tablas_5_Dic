from django.urls import path
from clientes_app import views

urlpatterns = [
    path("cliente", views.inicio_vistaCliente, name="cliente"),
    path("registrarCliente/", views.registrarCliente, name="registrarCliente"),
    path("seleccionarCliente/<int:id_cliente>", views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/", views.editarCliente, name="editarCliente"),
    path("borrarCliente/<int:id_cliente>", views.borrarCliente, name="borrarCliente"),
]

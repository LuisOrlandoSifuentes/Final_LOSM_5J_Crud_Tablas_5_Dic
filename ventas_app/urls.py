from django.urls import path
from ventas_app import views

urlpatterns = [
    path("ventas", views.inicio_ventas, name="ventas"),
    path("registrarVenta/", views.registrar_venta, name="registrarVenta"),
    path("seleccionarVenta/<int:id>", views.seleccionar_venta, name="seleccionarVenta"),
    path("editarVenta/", views.editar_venta, name="editarVenta"),
    path("borrarVenta/<int:id>", views.borrar_venta, name="borrarVenta"),
]

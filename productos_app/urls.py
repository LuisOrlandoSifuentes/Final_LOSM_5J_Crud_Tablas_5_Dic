from django.urls import path
from productos_app import views

urlpatterns = [
    path("producto", views.inicio_vistaProducto, name="producto"),
    path("registrarProducto/", views.registrarProducto, name="registrarProducto"),
    path("seleccionarProducto/<int:codigo>", views.seleccionarProducto, name="seleccionarProducto"),
    path("editarProducto/", views.editarProducto, name="editarProducto"),
    path("borrarProducto/<int:codigo>", views.borrarProducto, name="borrarProducto"),
]

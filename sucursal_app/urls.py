from django.urls import path
from . import views

urlpatterns = [
    path('sucursal', views.inicio_sucursal, name='sucursal'),
    path('registrarSucursal/', views.registrarSucursal, name='registrarSucursal'),
    path('seleccionarSucursal/<int:id_sucursal>/', views.seleccionarSucursal, name='seleccionarSucursal'),
    path('editarSucursal/', views.editarSucursal, name='editarSucursal'),
    path('borrarSucursal/<int:id_sucursal>/', views.borrarSucursal, name='borrarSucursal'),
]

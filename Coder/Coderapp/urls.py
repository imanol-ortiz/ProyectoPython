from django.urls import path

from Coderapp import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('producto/', views.VistaProducto, name="Producto"),
    path('vendedor/', views.VistaVendedor, name="Vendedor"),
    path('sucursal/', views.VistaSucursal, name="Sucursal"),
    path('buscarproductos/', views.BuscarProducto, name="BuscarProducto"),
]
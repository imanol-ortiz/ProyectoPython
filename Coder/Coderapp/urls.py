from django.urls import path

from Coderapp import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('producto/', views.Producto, name="Producto"),
    path('vendedor/', views.Vendedor, name="Vendedor"),
    path('sucursal/', views.Sucursal, name="Sucursal"),
]
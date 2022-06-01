from django.shortcuts import render, HttpResponse
from Coderapp.models import*

from Coderapp.forms import*

# Create your views here.

def Home(request):

        return render(request,"Coderapp/home.html")
    
def VistaProducto(request):

        if request.method=='POST':
                miformulario=ProductoFormulario(request.POST)
                print(miformulario)

                if miformulario.is_valid:
                        informacion=miformulario.cleaned_data
                        producto=Producto(nombre=informacion['nombre'], stock=informacion['stock'])
                        producto.save()
                        
                        return render(request,"Coderapp/home.html")
        else:
                miformulario=ProductoFormulario()
        
        return render(request,"Coderapp/producto.html", {"miformulario":miformulario})
    
def VistaVendedor(request):

        if request.method=='POST':
                miformulario=VendedorFormulario(request.POST)
                print(miformulario)

                if miformulario.is_valid:
                        informacion=miformulario.cleaned_data
                        vendedor=Vendedor(nombre=informacion['nombre'],apellido=informacion['apellido'],telefono=informacion['telefono'])
                        vendedor.save()
                        
                        return render(request,"Coderapp/home.html")
        else:
                miformulario=VendedorFormulario()
        
        return render(request,"Coderapp/vendedor.html", {"miformulario":miformulario})
    
def VistaSucursal(request):

        if request.method=='POST':
                miformulario=SucursalFormulario(request.POST)
                print(miformulario)

                if miformulario.is_valid:
                        informacion=miformulario.cleaned_data
                        sucursal=Sucursal(numero=informacion['numero'],direccion=informacion['direccion'])
                        sucursal.save()
                        
                        return render(request,"Coderapp/home.html")
        else:
                miformulario=SucursalFormulario()
        
        return render(request,"Coderapp/sucursal.html", {"miformulario":miformulario})

def BuscarProducto(request):
        
        if request.GET["nombre"]:
                nombre=request.GET["nombre"]
                producto=Producto.objects.filter(nombre__icontains=nombre)

                return render(request,"Coderapp/home.html", {"producto":producto, "nombre":nombre})
        else:
                respuesta="no hay datos"

        return render(request,"Coderapp/home.html", {"respuesta":respuesta})
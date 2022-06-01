from django.shortcuts import render, HttpResponse

from Coderapp.forms import*

# Create your views here.

def Home(request):

        return render(request,"Coderapp/home.html")
    
def Producto(request):

        if request.method=='POST':
                miformulario=ProductoFormulario(request.Post)
                print(miformulario)

                if miformulario.is_valid:
                        informacion=miformulario.cleaned_data
                        producto=Producto(nombre=['nombre'],stock=['stock'])
                        producto.save
                        
                        return render(request,"Coderapp/producto.html")
        else:
                miformulario=ProductoFormulario()
        
        return render(request,"Coderapp/producto.html", {"miformulario":miformulario})
    
def Vendedor(request):

        if request.method=='POST':
                miformulario=VendedorFormulario(request.Post)
                print(miformulario)

                if miformulario.is_valid:
                        informacion=miformulario.cleaned_data
                        vendedor=Vendedor(nombre=['nombre'],apellido=['apellido'],telefono=['telefono'])
                        vendedor.save
                        
                        return render(request,"Coderapp/vendedor.html")
        else:
                miformulario=VendedorFormulario()
        
        return render(request,"Coderapp/vendedor.html", {"miformulario":miformulario})
    
def Sucursal(request):

        if request.method=='POST':
                miformulario=SucursalFormulario(request.Post)
                print(miformulario)

                if miformulario.is_valid:
                        informacion=miformulario.cleaned_data
                        sucursal=Sucursal(numero=['numero'],direccion=['direccion'])
                        sucursal.save
                        
                        return render(request,"Coderapp/sucursal.html")
        else:
                miformulario=SucursalFormulario()
        
        return render(request,"Coderapp/sucursal.html", {"miformulario":miformulario})
from django.shortcuts import render, HttpResponse

# Create your views here.

def Home(request):

        return render(request,"Coderapp/home.html")
    
def Producto(request):

        return render(request,"Coderapp/producto.html")
    
def Vendedor(request):

        return render(request,"Coderapp/vendedor.html")
    
def Sucursal(request):

        return render(request,"Coderapp/sucursal.html")
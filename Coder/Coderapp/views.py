from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

        return render(request,"Coderapp/home.html")
    
def Cursos(request):

        return render(request,"Coderapp/cursos.html")
    
def Blog(request):

        return render(request,"Coderapp/blog.html")
    
def Contacto(request):

        return render(request,"Coderapp/contacto.html")
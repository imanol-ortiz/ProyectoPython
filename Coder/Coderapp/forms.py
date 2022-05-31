from django import forms

class ProductoFormulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    stock=forms.IntegerField()

class VendedorFormulario(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    telefono=forms.IntegerField()

class SucursalFormulario(forms.Form):
    numero=forms.IntegerField()
    direccion=forms.CharField(max_length=40)
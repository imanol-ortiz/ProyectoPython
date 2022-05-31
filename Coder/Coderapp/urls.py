from django.urls import path

from Coderapp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('cursos/', views.Cursos, name="Cursos"),
    path('blog/', views.Blog, name="Blog"),
    path('Contacto/', views.Contacto, name="Contacto"),
]
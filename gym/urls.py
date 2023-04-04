from django.urls import path
from gym import views

# Create your views here.
urlpatterns =[
    path('',views.home,name='Inicio'),
    # Read de los modelos
    path('profesor', views.Profesor, name='Profesor'),
    path('clase', views.Clase, name='Clase'),
    path('estudiante', views.Estudiante, name='Estudiante'),
    # Create de los modelos
    path('profesor/formulario',views.formProfesor,name='formProfesores'),
    path('clase/formulario',views.formClase,name='formClase'),
    path('estudiante/formulario',views.formEstudiantes,name='formEstudiantes'),
    # Delete de los modelos
    path('profesor/eliminar<nombre>',views.eliminarProfesor,name='eliminarProfe'),
    path('clase/eliminar<profesor>',views.eliminarClases,name='eliminarClase'),
    path('estudiante/eliminar<apellido>',views.eliminarEstudiante,name='eliminarEstu'),
    # Update de los modelos
    path('profesor/editar<nombre>',views.editarProfesor,name='editarProfesor'),
    path('clase/editar<profesor>',views.editarClase,name='editarClase'),
    path('estudiante/editar<correo>',views.editarEstudiante,name='editarEstudiante')
]
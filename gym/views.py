from django.shortcuts import render, HttpResponse,redirect
from .models import Profesores, Clases, Estudiantes
from .forms import FormProfesores, FormClase, FormEstudiante

def home(request):
    return render(request,'gym/home.html')


# Read de los modelos

def Profesor(request):    
    profesores = Profesores.objects.all()
    return render(request, 'gym/modelos/profesores.html', {'profesores':profesores})

def Clase(request):
    clases = Clases.objects.all()
    return render(request, 'gym/modelos/clases.html', {'clases':clases})

def Estudiante(request):
    estudiantes = Estudiantes.objects.all()
    return render(request, 'gym/modelos/estudiantes.html', {'estudiantes':estudiantes})

# Create de los modelos 

def formProfesor(request):
    if request.method == 'POST':
        formulario = FormProfesores(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            profesor = Profesores(nombre = informacion['nombre'],apellido = informacion['apellido'],correo = informacion['correo'],documento = informacion['documento']) # type: ignore
            profesor.save()
            return redirect('Profesor')
    else:
        formulario = FormProfesores()

    return render(request,'gym/formularios/formProfesores.html', {'formulario':formulario})

def formClase(request):
    if request.method == 'POST':
        formulario = FormClase(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            clase = Clases(nombre = informacion['nombre'],profesor = informacion['profesor'],dias = informacion['dias'],horario = informacion['horario']) # type: ignore
            clase.save()
            return redirect('Clase')
    else:
        formulario = FormClase()

    return render(request,'gym/formularios/formClase.html', {'formulario':formulario}) 

def formEstudiantes(request):
    if request.method == 'POST':
        formulario = FormEstudiante(request.POST)
        print(formulario)
        if formulario.is_valid:
            informacion = formulario.cleaned_data
            estudiante = Estudiantes(nombre = informacion['nombre'],apellido = informacion['apellido'],correo = informacion['correo'],pase = informacion['pase'],documento = informacion['documento'],fecha = informacion['fecha'])
            estudiante.save()
            return redirect('Estudiante')
    else:
        formulario = FormEstudiante()

    return render(request,'gym/formularios/formEstudiante.html', {'formulario':formulario})

# Delete de los modelos 

def eliminarProfesor(request,nombre):
    profesor = Profesores.objects.get(nombre=nombre)
    profesor.delete()
    return redirect('Profesor')

def eliminarClases(request,profesor):
    clase = Clases.objects.get(profesor=profesor)
    clase.delete()
    return redirect('Clase')

def eliminarEstudiante(request,apellido):
    estudiante = Estudiantes.objects.get(apellido=apellido)
    estudiante.delete()
    return redirect('Estudiante')

# Update de los modelos

def editarProfesor(request,nombre):

    profesor = Profesores.objects.get(nombre=nombre)

    if request.method == 'POST':

        miformulario = FormProfesores(request.POST)
        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data
            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.documento = informacion['documento']
            profesor.correo = informacion['correo']
            profesor.save()

            return redirect('Profesor')
    
    else:
        miformulario = FormProfesores(initial={'nombre':profesor.nombre,'apellido':profesor.apellido,'documento':profesor.documento,'correo':profesor.correo})
    
    return render(request,'gym/editar/editarProfesor.html',{'miformulario':miformulario,'profesor':profesor})


def editarClase(request,profesor):

    clase = Clases.objects.get(profesor=profesor)

    if request.method == 'POST':

        miformulario = FormClase(request.POST)
        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data
            clase.nombre = informacion['nombre']
            clase.profesor = informacion['profesor']
            clase.dias = informacion['dias']
            clase.horario = informacion['horario']
            clase.save()

            return redirect('Clase')
    
    else:
        miformulario = FormClase(initial={'nombre':clase.nombre,'profesor':clase.profesor,'dias':clase.dias,'horario':clase.horario})
    
    return render(request,'gym/editar/editarClase.html',{'miformulario':miformulario,'clase':clase})


def editarEstudiante(request,correo):

    estudiante = Estudiantes.objects.get(correo=correo)

    if request.method == 'POST':

        miformulario = FormEstudiante(request.POST)
        print(miformulario)

        if miformulario.is_valid:

            informacion = miformulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.correo = informacion['correo']
            estudiante.pase = informacion['pase']
            estudiante.documento = informacion['documento']
            estudiante.fecha = informacion['fecha']
            estudiante.save()

            return redirect('Estudiante')
    
    else:
        miformulario = FormEstudiante(initial={'nombre':estudiante.nombre,'apellido':estudiante.apellido,'correo':estudiante.correo,'pase':estudiante.pase,'documento':estudiante.documento,'fecha':estudiante.fecha})
    
    return render(request,'gym/editar/editarEstudiante.html',{'miformulario':miformulario,'estudiante':estudiante})
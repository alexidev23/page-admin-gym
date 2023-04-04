from django import forms

class FormProfesores(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    correo = forms.EmailField()
    documento = forms.IntegerField()

class FormClase(forms.Form):
    nombre = forms.CharField(max_length=40)
    profesor = forms.CharField(max_length=40)
    dias = forms.CharField(max_length=40)
    horario = forms.CharField(max_length=40)

class FormEstudiante(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    correo = forms.EmailField()
    pase = forms.CharField(max_length=30)
    documento = forms.IntegerField()
    fecha = forms.DateField()
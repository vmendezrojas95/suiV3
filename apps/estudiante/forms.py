from django import forms
from .models import Estudiante

class AddEstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('dni', 'legajo', 'nombre', 'apellido', 'correo', 'carrera', 'sexo')
        labels = {
            'dni': 'DNI Estudiante',
            'legajo': 'Legajo',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
            'carrera': 'Carrera',
            'sexo': 'Sexo',
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'legajo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }

class EditEstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ('dni', 'legajo', 'nombre', 'apellido', 'correo', 'carrera', 'estado', 'sexo')
        labels = {
            'dni': 'DNI Estudiante',
            'legajo': 'Legajo',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
            'carrera': 'Carrera',
            'estado': 'Estado',
            'sexo': 'Sexo',
        }
        widgets = {
            'dni': forms.TextInput(attrs={'type': 'text', 'id': 'dni_editar'}),
            'legajo': forms.TextInput(attrs={'type': 'text', 'id': 'legajo_editar'}),
            'nombre': forms.TextInput(attrs={'type': 'text', 'id': 'nombre_editar'}),
            'apellido': forms.TextInput(attrs={'type': 'text', 'id': 'apellido_editar'}),
            'correo': forms.EmailInput(attrs={'type': 'email', 'id': 'correo_editar'}),
            'carrera': forms.Select(attrs={'class': 'form-control', 'id': 'carrera_editar'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'estado_editar'}),
            'sexo': forms.Select(attrs={'class': 'form-control', 'id': 'sexo_editar'}),
        }

from django import forms
from .models import Docente

class AddDocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ('dni', 'nombre', 'apellido', 'correo', 'estado', 'sexo')
        labels = {
            'dni': 'DNI Docente',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
            'estado': 'Estado',
            'sexo': 'Sexo',
        }
        widgets = {
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }

class EditDocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ('dni', 'nombre', 'apellido', 'correo', 'estado', 'sexo')
        labels = {
            'dni': 'DNI Docente',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
            'estado': 'Estado',
            'sexo': 'Sexo',
        }
        widgets = {
            'dni': forms.TextInput(attrs={'type': 'text', 'id': 'dni_editar'}),
            'nombre': forms.TextInput(attrs={'type': 'text', 'id': 'nombre_editar'}),
            'apellido': forms.TextInput(attrs={'type': 'text', 'id': 'apellido_editar'}),
            'correo': forms.EmailInput(attrs={'type': 'email', 'id': 'correo_editar'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'estado_editar'}),
            'sexo': forms.Select(attrs={'class': 'form-control', 'id': 'sexo_editar'}),
        }

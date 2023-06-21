from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddEstudianteForm, EditEstudianteForm
from django.contrib import messages
from .models import Estudiante
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class EstudianteView(LoginRequiredMixin, View):
    def get(self, request):
        estudiantes = Estudiante.objects.all()
        form_estudiante = AddEstudianteForm()
        form_editar = EditEstudianteForm()
        context = {
            'estudiantes': estudiantes,
            'form_estudiante': form_estudiante,
            'form_editar': form_editar,
        }
        return render(request, 'estudiante.html', context)

class AddEstudianteView(LoginRequiredMixin, View):
    def post(self, request):
        print("Guardar estudiante")
        if request.method == 'POST':
            form_estudiante = AddEstudianteForm(request.POST)
            if form_estudiante.is_valid():
                try:
                    form_estudiante.save()
                except:
                    messages.error(request, 'Error al guardar el estudiante')  # Corrección aquí
                    return redirect('estudiante')
        return redirect('estudiante')


class EditEstudianteView(LoginRequiredMixin, View):
    def post(self, request):
        print("Editar estudiante")
        if request.POST:
            codigo_original = request.POST.get('dni_editar')
            print("Código del estudiante:", codigo_original)
            estudiante = Estudiante.objects.get(dni=codigo_original)
            print("Estudiante a editar:", estudiante)
            form_editar = EditEstudianteForm(request.POST, instance=estudiante)
            print("Formulario:", form_editar)
            if form_editar.is_valid():
                try:
                    print("Formulario válido")
                    form_editar.save()
                    print("Estudiante editado")
                    return redirect('estudiante')
                except:
                    messages(request, 'Error al editar el estudiante')
                    return redirect('estudiante')

class DeleteEstudianteView(LoginRequiredMixin, View):
    def post(self, request):
        print("Eliminar estudiante")
        if request.POST:
            codigo = request.POST.get('legajo_estudiante')
            print("Código del estudiante:", codigo)
            try:
                estudiante = Estudiante.objects.get(legajo=codigo)
                print("Estudiante encontrado:", estudiante)
                estudiante.delete()
                print("Estudiante eliminado")
                return redirect('estudiante')
            except Estudiante.DoesNotExist:
                print("Estudiante no encontrado")
                return redirect('estudiante')
        else:
            print("No se recibió una solicitud POST")
        return redirect('estudiante')

class DatosEstudianteView(LoginRequiredMixin, View):
    def get(self, request):
        estudiantes = Estudiante.objects.all()
        context = {
            'estudiantes': estudiantes,
        }
        return render(request, 'datos_estudiantes.html', context)


class DetalleEstudianteView(LoginRequiredMixin, View):
    def get(self, request, legajo):
        try:
            estudiante = Estudiante.objects.get(legajo=legajo)
            context = {
                'estudiante': estudiante,
            }
            return render(request, 'detalle_estudiante.html', context)
        except Estudiante.DoesNotExist:
            return redirect('datos_estudiantes')

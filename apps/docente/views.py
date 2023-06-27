from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddDocenteForm, EditDocenteForm
from django.contrib import messages
from .models import Docente
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class DocenteView(LoginRequiredMixin, View):
    def get(self, request):
        docentes = Docente.objects.all()
        form_docente = AddDocenteForm()
        form_editar = EditDocenteForm()
        context = {
            'docentes': docentes,
            'form_docente': form_docente,
            'form_editar': form_editar,
        }
        return render(request, 'docente.html', context)

class AddDocenteView(LoginRequiredMixin, View):
    def post(self, request):
        print("Guardar docente")
        if request.method == 'POST':
            form_docente = AddDocenteForm(request.POST)
            if form_docente.is_valid():
                try:
                    form_docente.save()
                except:
                    messages.error(request, 'Error al guardar el docente')
                    return redirect('docente')
        return redirect('docente')


class EditDocenteView(LoginRequiredMixin, View):
    def post(self, request):
        print("Editar docente")
        if request.POST:
            codigo_original = request.POST.get('dni_editar')
            print("Código del docente:", codigo_original)
            docente = Docente.objects.get(dni=codigo_original)
            print("Docente a editar:", docente)
            form_editar = EditDocenteForm(request.POST, instance=docente)
            print("Formulario:", form_editar)
            if form_editar.is_valid():
                try:
                    print("Formulario válido")
                    form_editar.save()
                    print("Docente editado")
                    return redirect('docente')
                except:
                    messages(request, 'Error al editar el docente')
                    return redirect('docente')

class DeleteDocenteView(LoginRequiredMixin, View):
    def post(self, request):
        print("Eliminar docente")
        if request.POST:
            codigo = request.POST.get('dni_docente')
            print("Código del docente:", codigo)
            try:
                docente = Docente.objects.get(dni=codigo)
                print("Docente encontrado:", docente)
                docente.delete()
                print("Docente eliminado")
                return redirect('docente')
            except Docente.DoesNotExist:
                print("Docente no encontrado")
                return redirect('docente')
        else:
            print("No se recibió una solicitud POST")
        return redirect('docente')

class DatosDocenteView(LoginRequiredMixin, View):
    def get(self, request):
        docentes = Docente.objects.all()
        context = {
            'docentes': docentes,
        }
        return render(request, 'datos_docentes.html', context)


class DetalleDocenteView(LoginRequiredMixin, View):
    def get(self, request, dni):
        try:
            docente = Docente.objects.get(dni=dni)
            context = {
                'docente': docente,
            }
            return render(request, 'detalle_docente.html', context)
        except Docente.DoesNotExist:
            return redirect('datos_docentes')

from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddCarreraForm, EditCarreraForm
from django.contrib import messages
from .models import Carrera
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class CarreraView(LoginRequiredMixin,View):
    def get(self, request):
        carreras = Carrera.objects.all()
        form_carrera = AddCarreraForm()
        form_editar = EditCarreraForm()
        context = {
            'carreras': carreras,
            'form_carrera': form_carrera,
            'form_editar': form_editar,
        }
        return render(request, 'carrera.html', context)

class AddCarreraView(LoginRequiredMixin,View):
    def post(self, request):
        print("Guardar Carrera")
        if request.method == 'POST':
            form_carrera = AddCarreraForm(request.POST, request.FILES)
            print("Formulario:", form_carrera)
            if form_carrera.is_valid():
                try:
                    form_carrera.save()
                except:
                    messages(request, 'Error al guardar la Carrera')
                    return redirect('carrera')
        return redirect('carrera')

class EditCarreraView(LoginRequiredMixin, View):
    def post(self, request):
        print("Editar carrera")
        if request.POST:
            codigo_original = request.POST.get('codigo_editar')
            print("Código de la carrera:", codigo_original)
            carrera = Carrera.objects.get(codigo=codigo_original)
            print("Carrera a editar:", carrera)
            form_editar = EditCarreraForm(request.POST, instance=carrera)
            print("Formulario:", form_editar)
            if form_editar.is_valid():
                try:
                    print("Formulario válido")
                    form_editar.save()
                    print("Carrera editada")
                    return redirect('carrera')
                except:
                    messages(request, 'Error al editar la carrera')
                    return redirect('carrera')

class DeleteCarreraView(LoginRequiredMixin, View):
    def post(self, request):
        print("Eliminar Carrera")
        if request.POST:
            codigo = request.POST.get('id_carrera')
            print("Código de la carrera:", codigo)
            try:
                carrera = Carrera.objects.get(codigo=codigo)
                print("Carrera encontrada:", carrera)
                carrera.delete()
                print("Carrera eliminada")
                print("Carrera:", carrera)
                return redirect('carrera')
            except Carrera.DoesNotExist:
                print("Carrera no encontrada")
                return redirect('carrera')
        else:
            print("No se recibió una solicitud POST")
        return redirect('carrera')

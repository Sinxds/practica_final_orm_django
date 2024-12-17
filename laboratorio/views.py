from django.shortcuts import render
from .models import Laboratorio, DirectorGeneral
from django.contrib import messages
from django.shortcuts import redirect



def index(request):
    contexto = {}
    return render(request, 'index.html', contexto)

# def laboratorio(request):
#     return render(request, 'laboratorio/laboratorio.html')

def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    contexto = {'laboratorios': laboratorios}

    return render(request, "laboratorio/listar_laboratorios.html", contexto)


def eliminar_laboratorio(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)

    if request.method == "POST":
        laboratorio.delete()
        messages.success(request, "Laboratorio eliminadop")
        return redirect('listar_laboratorios')
    else:
        contexto = {}
        contexto["laboratorio"] = laboratorio
        return render(request, 'laboratorio/eliminar_laboratorio.html', contexto)
    

def actualizar_laboratorio(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)

    if not laboratorio:
        messages.error(request, "El laboratorio no existe.")
        return redirect('listar_laboratorios')

    if request.method == 'POST':
        laboratorio.nombre = request.POST.get('nombre', laboratorio.nombre)
        laboratorio.ciudad = request.POST.get('ciudad', laboratorio.ciudad)
        laboratorio.pais = request.POST.get('pais', laboratorio.pais)
        laboratorio.save()

        messages.success(request, "Laboratorio actualizado correctamente.")
        return redirect('listar_laboratorios')
    
    contexto = {'laboratorio': laboratorio}

    return render(request, 'laboratorio/actualizar_laboratorio.html', contexto)

def agregar_laboratorio(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        ciudad = request.POST.get('ciudad', 'Sin ciudad')
        pais = request.POST.get('pais', 'Sin país')

        if not nombre:
            return render(request, 'laboratorio/agregar_laboratorio.html', {'error': 'El nombre es obligatorio'})

        Laboratorio.objects.create(
            nombre=nombre,
            ciudad=ciudad,
            pais=pais
        )
        return redirect('listar_laboratorios')

    return render(request, 'laboratorio/agregar_laboratorio.html')
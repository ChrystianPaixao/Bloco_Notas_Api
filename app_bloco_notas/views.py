from django.shortcuts import render, redirect, get_object_or_404
from .forms import NotasForm
from .models import Notas
from django.http import HttpRequest

def home(request):
    formulario = {
        "notas": Notas.objects.all()
    }
    return render(request, 'bloco_notas/home.html', formulario)

def adicionar_notas(request:HttpRequest):
    if request.method == 'POST':
        formulario = NotasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('notas:home')

    contexto = {
        "form": NotasForm
    }

    return render(request, 'bloco_notas/adicionar.html', contexto)

def remover_notas(id):
    notas = get_object_or_404(Notas, id=id)
    notas.delete()
    return redirect('notas:home')

def editar_notas(request:HttpRequest, id):
    notas = get_object_or_404(Notas, id=id)
    if request.method == 'POST':
        formulario = NotasForm(request.POST, instance=notas)
        if formulario.is_valid():
            formulario.save()
            return redirect('notas:home')
    formulario = NotasForm(instance=notas)
    contexto = {
        "form": formulario
    }
    return render(request, 'bloco_notas/editar.html', contexto)

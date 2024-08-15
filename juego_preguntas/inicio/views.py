from django.shortcuts import render
from usuarios.forms import  JugadorForm

def inicio(request):
    data = {}
    formulario = JugadorForm()
    data['formulario'] = formulario
    return render(request, 'inicio/inicio.html', data)

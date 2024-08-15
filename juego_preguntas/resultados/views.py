# views.py (resultados)
from django.shortcuts import render

def resultados(request):
    calificacion = request.session.get('calificacion', 0)
    return render(request, 'resultados/resultado.html', {'calificacion': calificacion})

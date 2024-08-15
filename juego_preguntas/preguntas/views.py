# views.py (preguntas)
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Pregunta, Respuesta

def preguntas(request):
    pagina = request.GET.get('pagina', 1)
    pregunta_aux = Pregunta.objects.all()
    paginador = Paginator(pregunta_aux, 1)  # 1 pregunta por página
    preguntas = paginador.get_page(pagina)

    if request.method == 'POST':
        calificacion = 0

        # Calcula la calificación
        for pregunta_id in preguntas.object_list.values_list('id', flat=True):
            respuesta_id = request.POST.get(f'respuesta_{pregunta_id}')
            if respuesta_id:
                respuesta = Respuesta.objects.get(id=respuesta_id)
                if respuesta.es_correcto:
                    calificacion += 1
        
        # Guarda la calificación en la sesión
        request.session['calificacion'] = calificacion

        # Redirige a la vista de resultados
        return redirect('resultados')

    context = {'preguntas': preguntas}
    return render(request, 'preguntas/preguntas.html', context)

def procesar_respuesta(request):
    return redirect('resultados')

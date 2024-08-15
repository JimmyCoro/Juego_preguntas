from django.contrib import admin

from preguntas.models import * 

modelos = [Pregunta, Respuesta]

admin.site.register(modelos)

from django.db import models
from usuarios.models import Jugador


class Pregunta(models.Model):
    DIFICULTAD = [
        ('facil', 'Fácil'),
        ('medio', 'Medio'),
        ('dificil', 'Difícil'),
    ]
    
    texto_pregunta = models.CharField(max_length=300)
    dificultad = models.CharField(max_length=8, choices=DIFICULTAD)

    @property
    def get_respuestas(self):
        return Respuesta.objects.filter(pregunta_id=self.id)
    
    def __str__(self):
        return self.texto_pregunta
    
class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas') 
    texto_respuesta = models.CharField(max_length=200)
    es_correcto = models.BooleanField(default=False)
    
    def __str__(self):
        return self.texto_respuesta
    
class Resultado(models.Model):
    usuario = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()
    tiempo = models.DurationField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    
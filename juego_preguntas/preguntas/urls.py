# urls.py (preguntas)
from django.urls import path
from .views import preguntas, procesar_respuesta

urlpatterns = [
    path('preguntas/', preguntas, name='preguntas'),
    path('procesar_respuesta/', procesar_respuesta, name='procesar_respuesta'),
]

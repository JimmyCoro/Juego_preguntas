from django.urls import path
from .views import save_jugador


urlpatterns = [
    path('save_jugador', save_jugador, name='save_jugador')
]
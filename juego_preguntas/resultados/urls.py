# urls.py (resultados)
from django.urls import path
from .views import resultados

urlpatterns = [
    path('resultados/', resultados, name='resultados'),
]

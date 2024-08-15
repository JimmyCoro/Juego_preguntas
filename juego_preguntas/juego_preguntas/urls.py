from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inicio.urls')),
    path('', include('preguntas.urls')),
    path('', include('resultados.urls')),
]

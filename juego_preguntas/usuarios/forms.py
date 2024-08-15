from django import forms
from .models import Jugador


class JugadorForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Jugador
        fields = ['correo', 'nombre', 'apellido']

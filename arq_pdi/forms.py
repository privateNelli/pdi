from django import forms
from .models import Caso

class CasoForm(forms.ModelForm):
    class Meta(object):
        model = Caso
        fields = ("tipo_caso", "ubicacion", "fono", "desc_caso")
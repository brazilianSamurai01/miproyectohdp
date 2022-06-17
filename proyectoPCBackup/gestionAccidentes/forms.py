from django import forms

from .models import DatosExtra, ReporteAccidente

class AccidenteForm(forms.ModelForm):
    descripcion=forms.CharField(widget=forms.Textarea(attrs={'rows':'3'}))
    class Meta:
        model=ReporteAccidente
        exclude=['user']

class DatosExtraForm(forms.ModelForm):
    class Meta:
        model=DatosExtra
        exclude=['accidente']
      
class FiltroForm(forms.Form):
    filtrar_por=forms.ChoiceField()
    filtro=forms.CharField()


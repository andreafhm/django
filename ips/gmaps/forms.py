from django import forms
from .models import Denuncia

Delitos = [
    ('Robo', 'Robo'),
    ('Asesinato', 'Asesinato'),
    (' ', ' '),
]

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = '__all__'
        widgets = {'DELITO': forms.Select(choices=Delitos)}
        widgets = {'FECHA': forms.DateInput(attrs={'type': 'date'})}


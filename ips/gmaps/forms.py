from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = '__all__'
        widgets = {'FECHA': forms.DateInput(attrs={ 'type' : 'date'})}

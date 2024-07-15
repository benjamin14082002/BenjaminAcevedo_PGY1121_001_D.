from django import forms
from .models import Medico, Horario, Reserva,Usuario
import pytz
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ('medico', 'horario',)

    def clean_horario(self):
        horario = self.cleaned_data['horario']
        if horario.disponible == False:
            raise forms.ValidationError('Este horario no está disponible')
        if horario.fecha < datetime.date.today():
            raise forms.ValidationError('No puedes seleccionar una fecha anterior a hoy')
        return horario
    

class UsuarioForm(UserCreationForm):
    tipoUsuario = forms.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES, label='Tipo de Usuario')

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['nombreUsuario', 'password1', 'password2', 'tipoUsuario']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.tipoUsuario = self.cleaned_data['tipoUsuario']
        if commit:
            user.save()
        return user
    
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de usuario'
        self.fields['password'].label = 'Contraseña'

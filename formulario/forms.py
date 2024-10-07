from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombres', 'apellidos', 'rut', 'email', 'direccion', 'comuna', 'telefono', 'mensaje']
        
        # Personaliza los widgets para añadir placeholder
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder': 'Ingresa nombres'}),
            'apellidos': forms.TextInput(attrs={'placeholder': 'Ingresa apellidos'}),
            'rut': forms.TextInput(attrs={'placeholder': 'Ejemplo: 12345678-9'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo electrónico'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingresa tu dirección'}),
            'comuna': forms.TextInput(attrs={'placeholder': 'Ingresa tu comuna'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingresa tu teléfono'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Escribe tu mensaje aquí...', 'rows': 4}),
        }

        widgets = {
            'mensaje': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Personaliza el widget del mensaje
        }

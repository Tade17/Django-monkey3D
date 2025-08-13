
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User as CustomUser 

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        label="Correo Electrónico",
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    phone_number = forms.CharField(
        label="Número de Teléfono",
        max_length=15,
        required=True, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    date_birth = forms.DateField(
        label="Fecha de Nacimiento",
        required=False, # O True si es obligatorio
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}) # Input de fecha HTML5
    )


    class Meta(UserCreationForm.Meta):
        model = CustomUser
        
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'date_birth',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields # Esto incluirá todos los campos del modelo CustomUser
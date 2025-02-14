from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Importa el modelo User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User  # Usa el modelo User de Django
        fields = ('username', 'email', 'first_name', 'last_name')
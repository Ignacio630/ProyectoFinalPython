from django import forms
from django.contrib.auth.models import User

class UserEditForm(forms.Form):
    username = forms.CharField(label='Modificar usuario', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Modificar email', required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Modificar nombre', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Modificar apellido', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserEditPasswordForm(forms.Form):
    password1 = forms.CharField(label='Modificar contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password1', 'password2']


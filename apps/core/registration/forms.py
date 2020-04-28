from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class RegisterForm (UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-user'})

        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Nombre'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Apellido'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['email'].widget.attrs['required'] = True
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password2'].widget.attrs['placeholder'] = 'Contraseña (confirmar)'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "El email ya esta registrado, prueba con otro")
        return email

    email = forms.EmailField(
        required=True, help_text='Requerido. 254 caracteres como máximo y debe ser válido')


class ProfileForm(forms.ModelForm):
    # TODO: Define form fields here
    class Meta:
        model = Profile
        fields = [
            'avatar',
            'biografia',
            'link',
            'fecha_nacimiento',
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            if not field == 'fecha_nacimiento':
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control form-control-user my-2'})
            else:
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control form-control-user my-2'})

        self.fields['biografia'].widget.attrs['placeholder'] = 'Bibliografía'
        self.fields['biografia'].widget.attrs['rows'] = 3


class EmailForm(forms.ModelForm):
    """Form definition for Email."""
    email = forms.EmailField(
        required=True, help_text='Requerido. 254 caracteres como máximo y debe ser válido')

    class Meta:
        """Meta definition for Emailform."""

        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {'class': 'form-control form-control-user my-2'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "El email ya esta registrado, prueba con otro")
        return email
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

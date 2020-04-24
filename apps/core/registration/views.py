from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#from django import forms

# Create your views here.


class RegisterCreateView(CreateView):

    form_class = RegisterForm

    template_name = "registration/register.html"

    def get_success_url(self):
        return reverse_lazy('login')+'?register'

    """
    def get_form(self, form_class=None):
        form = super(RegisterCreateView, self).get_form()

        # Modificamos en tiempo real

        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Usuario'})
        form.fields['first_name'].widget = forms.TextInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Nombre'})
        form.fields['last_name'].widget = forms.TextInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Apellido'})
        form.fields['email'].widget = forms.EmailInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Email', 'required': True})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Contraseña', 'required': True})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control form-control-user', 'placeholder': 'Contraseña (confirmar)', 'required': True})
        return form
    
    """


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(TemplateView):
    template_name = 'registration/profile.html'

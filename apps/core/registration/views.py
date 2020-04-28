from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import RegisterForm, ProfileForm, EmailForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

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
class ProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'registration/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        # recuperamos el objeto que se va a editar
        profile, created = Profile.objects.get_or_create(
            user=self.request.user)
        return profile


@method_decorator(login_required, name='dispatch')
class ProfileList(ListView):
    model = Profile
    #template_name = "registration/profile_list.html"
    paginate_by = 3


@method_decorator(login_required, name='dispatch')
class ProfileDetail(DetailView):
    model = Profile

    def get_object(self):
        # recuperamos el objeto que se va a editar
        return get_object_or_404(Profile, user__username=self.kwargs['username'])


@method_decorator(login_required, name='dispatch')
class ProfileEmailUpdate(UpdateView):
    model = User
    form_class = EmailForm
    template_name = "registration/profile_email_form.html"
    success_url = reverse_lazy('profile')

    def get_object(self):
        # recuperamos el objeto que se va a editar
        return self.request.user

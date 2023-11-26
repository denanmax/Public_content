from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, FormView, CreateView
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from users.forms import UserRegisterForm, UserProfileForm, UserLoginForm
from users.models import User

class CustomLoginView(FormView):
    """Контроллер входа пользователя"""
    model = User
    template_name = 'users/login.html'
    form_class = UserLoginForm
    extra_context = {
        'title': 'Войти'
    }



class RegisterView(CreateView):
    """Контроллер регистрации пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    extra_context = {
        'title': 'Регистрация'
    }



class ProfileView(UpdateView):
    """Обновление профиля"""
    model = User
    form_class = UserProfileForm
    extra_context = {
        'title': 'Данные профиля'
    }

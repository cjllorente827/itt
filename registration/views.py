import json

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password':forms.PasswordInput(),
    }

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    widgets = {
        'password' :forms.PasswordInput(),
        'password2' :forms.PasswordInput(),
    }

    def is_valid(self):
        if not super(RegisterForm, self).is_valid():
            return False
        elif self.cleaned_data['password'] != self.cleaned_data['password2']:
            return False
        return True


def index(request):
    return HttpResponseRedirect('')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/t')
            return HttpResponseRedirect('/errorMsg/403')
    else:
        form = LoginForm()

    return HttpResponseRedirect('/')

def user_logout(request):
    if request.method == 'GET':
        logout(request)
    return HttpResponseRedirect('/')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            user = User.objects.create_user(username, None, password)
            user.save()

            if user is not None and user.is_active:
                return HttpResponseRedirect('/errorMsg/200')
            return HttpResponseRedirect('/errorMsg/404')
    else:
        form = RegisterForm()

    response = render(request, 'registration/auth_panel.html', {
        'form': form,
    })
    return response
    
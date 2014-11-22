import json

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=25)
    password = forms.CharField(max_length=25)
    password2 = forms.CharField(max_length=25)

    def is_valid(self):
        if not super(RegisterForm, self).is_valid():
            return False
        elif self.cleaned_data['password'] != self.cleaned_data['password2']:
            return False
        return True

def renderSideBar(request):
    if request.user.is_authenticated():
        return "You are logged in as " + request.user.username
    return LoginForm()

def index():
    return HttpResponseRedirect('')

def get_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/threads/')
            return HttpResponseRedirect('/errorMsg/404')
    else:
        form = LoginForm()

    return HttpResponseRedirect('')

def register(request):
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

    response = render(request, 'login/register.html', {
        'form': form,
        'sidebar' : renderSideBar(request),
    })
    return response
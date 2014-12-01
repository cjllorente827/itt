from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

import json

from authorization.forms import LoginForm, RegisterForm

def user_login(request):	
	print(request.POST)
	form = LoginForm(request.POST).get_validation()

	if not form["valid"]:
		return HttpResponse(form['reason'], None, form['status'])
	
	user = authenticate(
		username=form['username'], 
		password=form['password'])

	if user is not None and user.is_active:
		login(request, user)
		return HttpResponseRedirect('/t')
	return HttpResponse('Invalid username or password', None, 200)

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def create_user(request):
	
	form = RegisterForm(request.POST).get_validation() 
	if not form["valid"]:
		return HttpResponse(form['reason'], None, form['status'])

	user = User.objects.create_user(form['username'], None, form['password'])
	user.save()
	
	return HttpResponse(''.join(['User ', user.username, ' created']), None, 201)
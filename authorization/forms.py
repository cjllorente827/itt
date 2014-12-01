from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(max_length=25)
	password = forms.CharField(max_length=25)
	#is_bound = False

	def get_validation(self):
		if not super(LoginForm, self).is_valid():
			return {
				"valid" : False,
				"reason" : "Validation error",
				"status" : 403}
		return {
			"valid" : True,
			"username" : self.cleaned_data["username"],
			"password" : self.cleaned_data["password"],
			"status" : 200}

class RegisterForm(forms.Form):
	username = forms.CharField(max_length=25)
	password = forms.CharField(max_length=25)
	password2 = forms.CharField(max_length=25)
	
	def get_validation(self):
		if not super(RegisterForm, self).is_valid():
			return {
				"valid" : False,
				"reason" : "Validation error",
				"status" : 403}
		elif self.cleaned_data["password"] != self.cleaned_data["password2"]:
			return {
				"valid" : False,
				"reason" : "Passwords do not match",
				"status" : 400}
		return {
			"valid" : True,
			"username" : self.cleaned_data["username"],
			"password" : self.cleaned_data["password"],
			"status" : 200}
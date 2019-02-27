# main_app/forms.py
from django import forms
from .models import User, Day, Moment
from django.forms import ModelForm

class DayForm(forms.Form):
	date = forms.DateField(label="date")
	chill_score = forms.DecimalField(label="chill score")

class MomentForm(forms.Form):
	desc = forms.CharField(label="what")
	where = forms.CharField(label="where")

class LoginForm(forms.Form):
	username = forms.CharField(label="User name", max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())

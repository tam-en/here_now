# main_app/forms.py
from django import forms
from .models import User, Day, Moment
import datetime
# from django.forms import ModelForm

class DayForm(forms.ModelForm):
	class Meta:
		model = Day
		fields = ['chill_score']

class SimpleDayForm(forms.Form):
	date = forms.DateField(label = 'date')
	chill_score = forms.DecimalField(label = 'chill score', decimal_places=1,max_digits=3)

class MomentForm(forms.ModelForm):
	class Meta:
		model = Moment
		fields = ['desc', 'where', 'when']

class LoginForm(forms.Form):
	username = forms.CharField(label="User name", max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())

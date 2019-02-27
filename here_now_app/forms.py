# main_app/forms.py
from django import forms
from .models import User, Day, Moment
# from django.forms import ModelForm

class DayForm(forms.ModelForm):
	class Meta:
		model = Day
		fields = ['date', 'chill_score']
	# date = forms.DateField(label="date")
	# chill_score = forms.DecimalField(label="chill score")

class MomentForm(forms.ModelForm):
	class Meta:
		model = Moment
		fields = ['desc', 'where']
	# desc = forms.CharField(label="what")
	# where = forms.CharField(label="where")

class LoginForm(forms.Form):
	username = forms.CharField(label="User name", max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())

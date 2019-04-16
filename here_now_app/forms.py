# main_app/forms.py
from django import forms
from .models import User, Day, Moment
import datetime
# import floppyforms as forms

# from django.forms import ModelForm

class DayForm(forms.ModelForm):
	class Meta:
		model = Day
		fields = ['chill_score']


# class MomentForm(forms.Form):
# 	desc = forms.CharField(label='description')
# 	where = forms.CharField(label='where')
# 	when = forms.IntegerField(label='')


# class DayForm(forms.Form):
# 	date = forms.DateField(label = 'date')
# 	chill_score = forms.DecimalField(label = 'chill score', decimal_places=1,max_digits=3)

# class SimpleDayForm(forms.Form):
# 	# date = forms.DateField(label = 'date')
# 	date = datetime.datetime.today().date()
# 	# chill_score = forms.DecimalField(label = 'chill score', decimal_places=1,max_digits=3)	

class MomentForm(forms.ModelForm):
	class Meta:
		model = Moment
		fields = ['desc', 'where', 'when']

class LoginForm(forms.Form):
	username = forms.CharField(label="User name", max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())

## stuff from documentation:

# class Slider(forms.RangeInput):
#     min = 0
#     max = 10
#     step = .1
#     template_name = 'today.html'

	# class Media:
	# 	js = (
	# 		'js/jquery.min.js',
	# 		'js/jquery-ui.min.js',
	# 	)
	# 	css = {
	# 		'all': (
	# 		'css/jquery-ui.css',
	# 		)
	# 	}


# class SlideForm(forms.Form):
#     num = forms.DecimalField(widget=Slider)

#     def clean_num(self):
#         num = self.cleaned_data['num']
#         if not 0 <= num <= 10:
#             raise forms.ValidationError("Enter a value between 0 and 10")
#         return num	

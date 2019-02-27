import datetime
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.
class Day(models.Model):
	date = models.DateField('day described')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	chill_score = models.DecimalField(decimal_places=1,max_digits=3, default=5.0)

	def __str__(self):
		return self.date.strftime("%Y%m%d (%A, %b %d, %Y)")

class DayForm(ModelForm):
	class Meta:
		model = Day
		fields = ['date', 'chill_score', 'user']

class Moment(models.Model):
	desc = models.CharField(max_length=200)
	where = models.CharField(max_length=50)
	when = models.ForeignKey(Day, on_delete=models.CASCADE)

	def __str__(self):
		return self.desc

class MomentForm(ModelForm):
	class Meta:
		model = Moment
		fields = ['desc', 'where']
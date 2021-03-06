import datetime
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.
class Day(models.Model):
	date = models.DateField('day described', default=datetime.datetime.now)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	chill_score = models.DecimalField(decimal_places=1,max_digits=3, default=5.0)

	# def __str__(self):
	# 	return self.date.strftime("%A, %b %d, %Y")

class Moment(models.Model):
	desc = models.CharField(max_length=200)
	where = models.CharField(max_length=50)
	when = models.ForeignKey(Day, on_delete=models.CASCADE)

	def __str__(self):
		return self.desc

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Day, Moment
from .forms import LoginForm, DayForm, MomentForm # SimpleDayForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
import datetime

def index(request):
	return render(request, 'index.html')

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect('/today', {'user': user})
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})

def login_view(request):
	context = {'error':False}
	if request.method == 'POST':
		# if post, then authenticate (user submitted username and password)
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user. is_active:
					login(request, user)
					return HttpResponseRedirect('/today', {'user': user})
				else:
					print("The account has been disabled.")
			else:
				print("The username and/or password is incorrect.")
				# just added this:
				form = LoginForm()
				return render(request, 'login.html', {'form': form}) 
			
	else:
		print('step five')
		form = LoginForm()
		return render(request, 'login.html', {'form': form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def profile(request):
	return render(request, 'profile.html')

def about(request):
	return render(request, 'about.html')

def today(request):
	print("today route request.POST:", request.POST)
	print("today route request.GET:", request.GET)
	print("request at beginning of today=", request)
	print(request.user.id, "heya!")

	days = list(Day.objects.filter(user_id=request.user.id)) # to convert days from query string to list
	now = datetime.datetime.today().date()
	print("trying something", datetime.datetime.today().date())
	print("ZZZZZZZ now is", now)
	today_exists = False
	today_day = None
	user_today_id = None
	moments = None
	for day in days:
		if day.date == now:
			today_exists = True
			today_day_list = list(Day.objects.filter(user_id=request.user.id).filter(date=now))
			today_day = ','.join(str(s) for s in today_day_list)
			today_day = list(today_day.split())
			today_day = list(today_day[len(today_day)-1])
			today_day.remove('(')
			today_day.remove(')')
			today_day = ''.join(str(s) for s in today_day)
			today_day = int(today_day)
			# Day.objects.filter(user_id=request.user.id).filter(date=now)	
	if today_day:
		moments = list(Moment.objects.filter(when_id=today_day))
	form1 = DayForm()
	form2 = MomentForm()
	# form3 = SimpleDayForm()
	if moments:
		return render(request, 'today.html', {'form1': form1, 'form2': form2, 'days': days, 'now': now, 'today_exists': today_exists, 'today_day': today_day, 'moments': moments})
	else:
		return render(request, 'today.html', {'form1': form1, 'form2': form2, 'days': days, 'now': now, 'today_exists': today_exists, 'today_day': today_day})		

def post_day(request):
	print("post_day route:", request.POST)
	form1 = DayForm(request.POST)
	if form1.is_valid():
		day = form1.save(commit=False)
		day.user_id = request.user.id
		day.save()
		return HttpResponseRedirect('/today')

# def post_day(request):
# 	print("post_day route:", request.POST)
# 	# save_user = SimpleDayForm(user=request.user)
# 	# form = SimpleDayForm(request.POST, instance=save_user)
# 	form = SimpleDayForm(request.POST)
# 	if form.is_valid():
# 		day = form.save(commit = False)
# 		# day.date = datetime.datetime.today().date()
# 		# day.user_id = request.user.id
# 		# day.chill_score = request.chill_score
# 		day.save()
# 		return HttpResponseRedirect('/today')

# def post_day(request):
# 	print("post_day new HTML plain route:", request.POST)
# 	print("server generated date=", datetime.datetime.today().date())
# 	print(request.user.id, "heya again!!!!!!")
# 	# user_id = request.user.id
# 	# date = datetime.datetime.today().date()
# 	# chill_score = request.chill_score
# 	# context = {}

# 	return HttpResponseRedirect('/today')

def post_moment(request):
	print("hitting the post_moment route")
	print(request.POST)
	form = MomentForm(request.POST)
	if form.is_valid():
		moment = form.save(commit = False)
		moment.save()
		return HttpResponseRedirect('/today')


def before(request):
	days = list(Day.objects.filter(user_id=request.user.id).order_by('-date')) # to convert days from query string to list
	now = datetime.datetime.today().date()
	if(days):
		return render(request, 'before.html', {'days': days, 'now': now })
	else:
		return render(request, 'before.html', {'days': None, 'now': now })


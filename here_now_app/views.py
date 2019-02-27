from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Day, Moment
from .forms import LoginForm, DayForm, MomentForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def index(request):
	# cats = Cat.objects.all()
	# form = CatForm()
	# return HttpResponse('<h1>hi there.</h1>')
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
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
	context = {'error':False}
	print('step one')
	if request.method == 'POST':
		# if post, then authenticate (user submitted username and password)
		print('step two')
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			print('step three, user=')
			if user is not None:
				if user. is_active:
					print('step four')
					login(request, user)
					print('step five')
					return HttpResponseRedirect('/today', {'user': user})
				else:
					print("The account has been disabled.")
			else:
				print("The username and/or password is incorrect.")
	else:
		print('step five')
		form = LoginForm()
		return render(request, 'login.html', {'form': form})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

def profile(request, username):
	user = User.objects.get(username=username)
	return render(request, 'profile.html', {'username': username })

def about(request):
	return render(request, 'about.html')

def today(request, user_id):
	form = DayForm()
	return render(request, 'today.html', {'form': form})

def post_today(request):
	print("request=", request)
	print("user.id=", user.id)
	form = DayForm(request.POST)
	if form.is_valid():
		day = form.save(commit = False)
		day.date = request.date
		day.chill_score = request.chill_score
		day.user_id = user.id
		day.save()
	return HttpResponseRedirect('/today')

def day(request, day_id):
	day = Day.objects.get(id=day_id)
	moments = list(Moment.objects.filter(when_id=day_id))
	return render(request, 'day.html', {'day': day, 'moments': moments})	

def before(request, user_id):
	days = list(Day.objects.filter(user_id=user_id)) # to convert days from query string to list
	if(days):
		for day in days:
			moments = list(Moment.objects.filter(when_id=day.id))	
		return render(request, 'before.html', {'days': days, 'moments':moments})
	else:
		return render(request, 'before.html', {'days': days, 'moments':None})




from django.urls import path
from . import views
# from herenow.core import views as core_views

# url patterns look like this:
# path(<url pattern>, <view>, name=<route name>)

urlpatterns = [
	# ex: /here_now_app/
	path('', views.index, name="index"), # home/landing page route
	path('profile/', views.profile, name='profile'),
	path('login/', views.login_view, name="login"),
	path('logout/', views.logout_view, name="logout"),
	path('signup', views.signup, name="signup"),
	path('about', views.about, name="about"),
	path('day/<int:day_id>', views.day, name="day"),
	path('today', views.today, name="today"),
	path('post_today', views.post_today, name="post_today"),
	# path('before/<user_id>', views.before, name='before')
	path('before/', views.before, name='before')
]



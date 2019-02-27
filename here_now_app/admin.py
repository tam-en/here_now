from django.contrib import admin

# Register your models here.
from .models import Day
from .models import Moment

admin.site.register(Day)
admin.site.register(Moment)

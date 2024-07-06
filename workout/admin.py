from django.contrib import admin

from workout.models import Workout, Exercise

# Register your models here.

admin.site.register(Workout)
admin.site.register(Exercise)
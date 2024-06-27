from django.contrib import admin

from .models import GymUser, Trainer, Client

# Register your models here.

admin.site.register(GymUser)
admin.site.register(Trainer)
admin.site.register(Client)
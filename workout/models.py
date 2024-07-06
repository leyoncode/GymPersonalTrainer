from django.core.validators import MaxValueValidator
from django.db import models

from user.models import Trainer, Client


class Workout(models.Model):
    name = models.CharField(max_length=100, verbose_name="Workout Name")
    description = models.TextField(verbose_name="Workout Description", help_text="Detailed description of the workout.")
    days_per_week = models.PositiveIntegerField(validators=[MaxValueValidator(7)], verbose_name="Days per Week")

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, verbose_name="Trainer")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client")

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=100, verbose_name="Exercise Name")
    sets = models.PositiveIntegerField(verbose_name="Number of Sets")
    reps = models.PositiveIntegerField(verbose_name="Number of Reps")
    tutorial_url = models.URLField(verbose_name="Tutorial URL")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, verbose_name="Associated Workout")

    def __str__(self):
        return f"{self.name} ({self.workout.name})"
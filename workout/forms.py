from django import forms
from .models import Workout, Exercise


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'description', 'days_per_week', 'trainer', 'client']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'tutorial_url', 'workout']
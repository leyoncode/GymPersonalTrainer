from django import forms

from user.models import Client
from .models import Workout, Exercise


class WorkoutForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        trainer = kwargs.pop('trainer', None)
        super(WorkoutForm, self).__init__(*args, **kwargs)
        if trainer:
            # Filter clients based on the trainer's association
            self.fields['client'].queryset = Client.objects.filter(trainer=trainer)

    class Meta:
        model = Workout
        fields = ['name', 'description', 'days_per_week', 'client']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'tutorial_url']

    def __init__(self, *args, **kwargs):
        super(ExerciseForm, self).__init__(*args, **kwargs)
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import GymUser, Trainer, Client


class GymUserRegistrationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=GymUser.USER_TYPE_CHOICES)

    class Meta:
        model = GymUser
        fields = ['username', 'email', 'user_type', 'password1', 'password2']


class GymUserLoginForm(AuthenticationForm):
    class Meta:
        model = GymUser
        fields = ['username', 'password']


class TrainerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['contact', 'website']


class ClientRegistrationForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['contact', 'age', 'weight_in_lbs', 'reason_for_training', 'gender']
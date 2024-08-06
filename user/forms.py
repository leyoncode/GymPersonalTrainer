from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import GymUser, Trainer, Client
from django.core.exceptions import ValidationError


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
        fields = ['trainer_contact', 'website']


# class ClientRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = Client
#         fields = ['user_contact', 'age', 'weight_in_lbs', 'reason_for_training', 'gender', 'trainer']
#
class ClientRegistrationForm(forms.ModelForm):
    trainer_username = forms.CharField(required=True, help_text="Enter your trainer's username.")

    class Meta:
        model = Client
        fields = ['user_contact', 'age', 'weight_in_lbs', 'reason_for_training', 'gender', 'trainer_username']

    def clean_trainer_username(self):
        username = self.cleaned_data.get('trainer_username')
        try:
            trainer = Trainer.objects.get(user__username=username)
            print("No error detected")
            return trainer
        except Trainer.DoesNotExist:
            print("Errror detected")  # DEBUG
            raise forms.ValidationError("A trainer with this username does not exist.")

    def save(self, commit=True):
        client = super(ClientRegistrationForm, self).save(commit=False)
        # Set the trainer to the Trainer object fetched from the cleaned data
        client.trainer = self.cleaned_data.get('trainer_username')

        if commit:
            client.save()

        return client
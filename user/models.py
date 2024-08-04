from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class GymUser(AbstractUser):
    TRAINER = 'Trainer'
    CLIENT = 'Client'

    USER_TYPE_CHOICES = {
        TRAINER: 'Trainer',
        CLIENT: 'Client'
    }
    user_type = models.CharField(max_length=7, choices=USER_TYPE_CHOICES, default=CLIENT)

    email = models.EmailField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.username


class Trainer(models.Model):
    user = models.OneToOneField(GymUser, on_delete=models.CASCADE, primary_key=True)

    trainer_contact = models.CharField(max_length=20)  # phone numbers
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.user.username


class Client(models.Model):
    user = models.OneToOneField(GymUser, on_delete=models.CASCADE, primary_key=True)

    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    user_contact = models.CharField(max_length=20)  # phone numbers
    age = models.PositiveIntegerField(default=0)
    weight_in_lbs = models.PositiveIntegerField(default=0)
    reason_for_training = models.CharField(null=True, blank=True, max_length=255)

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'  # Other here means 'other' or prefer not to answer

    GENDER_CHOICES = {
        MALE: 'Male',
        FEMALE: 'Female',
        OTHER: 'Other',
    }

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=OTHER)

    def __str__(self):
        return self.user.username
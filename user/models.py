from django.db import models


# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()  #email
    contact = models.CharField(max_length=20)  #phone numbers
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    age = models.PositiveIntegerField(default=0)

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    GENDER_CHOICES = {
        MALE: 'Male',
        FEMALE: 'Female',
        OTHER: 'Other',
    }

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=OTHER)

    def __str__(self):
        return self.name
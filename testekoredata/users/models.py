from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\+?\d{10,15}$',
    message="Enter a valid phone number."
)

class User(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    adress = models.CharField(max_length=300)
    phone = models.CharField(max_length=20, validators=[phone_validator])

    def __str__(self):
        return self.fullname
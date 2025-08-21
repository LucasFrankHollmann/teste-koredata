from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    fullname = models.CharField(max_length=200)
    email = models.EmailField()
    adress = models.CharField(max_length=300)
    phone = PhoneNumberField(region="BR")

    def __str__(self):
        return self.fullname
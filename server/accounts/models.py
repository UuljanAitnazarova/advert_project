from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    phone_regex = RegexValidator(regex=r'^\+996\w{9}$',
                                 message="Phone number must be entered in the format: '+996xxxxxxxxx'. Up to 12 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=False, null=False)

    def __str__(self):
        return f'{self.user}: {self.phone_number}'
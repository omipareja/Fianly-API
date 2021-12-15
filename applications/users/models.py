from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .choices import GENDER_CHOICES
from .managers import UserManager


# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    def __str__(self):
        return str(self.pk) + '-' + self.first_name

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    patronym = models.CharField(
        _('patronym'),
        max_length=150,
    )
    edu_institution = models.CharField(
        _('educational institution'),
        max_length=200,
    )
    email = models.EmailField(
        _('email address'),
        unique=True,
    )
    phone_number = PhoneNumberField(
        _('phone number'),
        unique=True,
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = False


User = get_user_model()

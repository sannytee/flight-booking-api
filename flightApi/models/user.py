""" User model """

# pylint: disable=too-few-public-methods

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from flightApi.models.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ User Model"""

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile_picture = models.CharField(max_length=500)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        """Define metadata options."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """ Return object's string representation """
        return f'{self.first_name} {self.last_name}'

    @property
    def is_superuser(self):
        """Check whether user is super admin"""
        return self.admin

    @property
    def is_staff(self):
        """Check whether user is staff"""
        return self.staff

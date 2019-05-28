"""Create the user manager model """

from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ User model manager """

    def create_user(self,
                    email,
                    password,
                    is_staff=False,
                    is_admin=False):
        """
        Creates and saves a user with the given email and password
        """
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.staff = is_staff
        user.admin = is_admin
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        """ creates a super user"""
        return self.create_user(
            email,
            is_admin=True,
            is_staff=True,
            password=password
        )

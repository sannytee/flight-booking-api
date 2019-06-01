"""Base test functionality"""

from django.contrib.auth.base_user import make_password
from rest_framework.test import APITestCase

from flightApi.models import User


# pylint: disable=no-member
class BaseTestCase(APITestCase):
    """Base testing functionality"""

    @classmethod
    def setUp(cls):
        """Initialize testing database"""
        cls.test_user = User.objects.create(
            first_name='new',
            last_name='user',
            email='newuser@mail.com',
            password=make_password('password'),
            profile_picture='picture_url'
        )
        cls.test_user.save()

    def test_client(self, token=None):
        """Create a test client with an optional token"""
        client = self.client
        client.credentials()
        if token:
            client.credentials(HTTP_AUTHORIZATION=token)
        return client

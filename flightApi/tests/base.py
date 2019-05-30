"""Base test functionality"""

from rest_framework.test import APITestCase


class BaseTestCase(APITestCase):
    def test_client(self, token=None):
        """Create a test client with an optional token"""
        client = self.client
        client.credentials()
        if token:
            client.credentials(HTTP_AUTHORIZATION=token)
        return client

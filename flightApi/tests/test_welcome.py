"""Tests for default api"""
from flightApi.tests.base import BaseTestCase


class TestWelcome(BaseTestCase):
    """ Test for the welcome view function. """
    def test_view_welcome_api(self):
        """Test the output of the root api"""
        response = self.test_client().get('/')
        data = {
            "status": "success",
            "message": "Welcome to the Flight API"
        }
        self.assertEqual(200, response.status_code)
        self.assertDictEqual(response.data, data)

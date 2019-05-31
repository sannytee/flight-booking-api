"""Test models are working properly"""
import pytest

from rest_framework.test import APITestCase
from flightApi.models import User


class ModelTest(APITestCase):
    """Model test case"""

    def setUp(self):
        """models to be created during setup"""
        self.new_user = User(first_name="new",
                             last_name="user",
                             email="new_user@mail.com",
                             profile_picture='some_url',
                             )

    def test_models_can_create_user(self):
        """Test creation of user"""
        self.new_user.save()
        user_count = User.objects.count()
        self.assertEqual(1, user_count)

    def test_user_manager_can_create_super_user(self):
        """Test creation of admin user"""
        admin = User.objects.create_superuser(email='admin@mail.com',
                                              password='password')
        self.assertEqual(admin.staff, True)

    def test_user_manager_fail_without_email(self):
        """Test user cannot be created without email"""
        with pytest.raises(ValueError, match='User must have an email address'):
            test_user = User.objects.create_user(email="", password='')
            self.assertEqual(test_user, None)

    def test_user_is_staff_property_can_be_accessed(self):
        """Test property is_staff can be accessed"""
        user = self.new_user
        self.assertEqual(user.is_staff, False)

    def test_user_is_suoeruser_property_can_be_accessed(self):
        """Test property is_admin can be accessed"""
        user = self.new_user
        self.assertEqual(user.is_superuser, False)

    def test_user_model_return_user_string_representation(self):
        """ Test user string representation """
        user = self.new_user
        self.assertEqual(str(user), "new user")

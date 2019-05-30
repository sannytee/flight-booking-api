""" helper functions """
import cloudinary.uploader

from rest_framework_jwt.settings import api_settings


def generate_token(user):
    """Helper function to generate token for a user"""
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    return token


def upload_image(image):
    """ Helper function to upload an image to cloudinary"""
    response = cloudinary.uploader.upload(image)
    return response['url']

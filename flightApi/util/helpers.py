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


def check_user_input(required_field, user_input):
    """ Helper function to check for required field in user input"""
    message = ''
    for field in required_field:
        if field not in user_input.keys():
            message += field + ', '
    if message:
        return 'check if the {} field exist'.format(message[:-2])
    return None

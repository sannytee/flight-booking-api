""" helper functions """
import random
from datetime import datetime, timedelta

import cloudinary.uploader
from django.conf import settings
from django.core.mail import send_mail
from rest_framework_jwt.settings import api_settings


def generate_token(user):
    """Helper function to generate token for a user"""
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    token = jwt_encode_handler({'username': user.email,
                                'exp': datetime.utcnow() + timedelta(days=1)
                                })
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


def get_flight_and_time():
    """ get a random flight from flights"""
    flights = ['FT 901', 'FT 807', 'FT 609']
    flight_time = ['13:45:00', '21:00:00', '09:00:00', '10:00:00', '18:00:00']
    flight_id = random.randint(0, 2)
    flight_time_id = random.randint(0, 4)
    return flights[flight_id], flight_time[flight_time_id]


def filter_flight_field(flight_response, field):
    """ filters the flight field"""
    filtered_response = {
        x:  flight_response.get(x) for x in field if x in flight_response
    }
    return filtered_response


def send_booking_ticket_mail(subject, email, msg):
    """send ticket to user mail"""
    subject = subject
    from_email = settings.EMAIL_HOST_USER
    to_email = [email]
    message = msg
    send_mail(subject=subject, from_email=from_email,
              recipient_list=to_email, message=message, fail_silently=True)

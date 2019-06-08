""" create tasks event here"""
from celery import shared_task
from celery.utils.log import get_task_logger

from flightApi.util.helpers import send_booking_ticket_mail

# pylint: disable=invalid-name
logger = get_task_logger(__name__)


@shared_task(name="send_ticket_booking")
def send_booking_email_task(email, message):
    """sends email after booking is successful"""
    logger.info("sent booking email")
    return send_booking_ticket_mail(email, message)

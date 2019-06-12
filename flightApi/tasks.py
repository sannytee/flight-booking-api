""" create tasks event here"""
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from celery import shared_task
from celery.utils.log import get_task_logger

from flightApi.models import Flight
from flightApi.util.helpers import send_booking_ticket_mail

# pylint: disable=invalid-name, no-member
logger = get_task_logger(__name__)


@shared_task(name="send_ticket_booking")
def send_booking_email_task(subject, email, message):
    """sends email after booking is successful"""
    logger.info("sent booking email")
    return send_booking_ticket_mail(subject, email, message)


def send_email_reminders():
    """ send email to remind user of their upcoming flight"""
    flight_day = datetime.now() + timedelta(days=1)
    flights = Flight.objects.select_related('passenger').filter(departure_date=flight_day)
    for ticket in flights:
        email = ticket.passenger.email
        subject = "Flight Travel Reminder"
        content = f'Kindly take note that your flight is next 24 hours'
        send_booking_email_task.delay(subject, email, content)


def start_process():
    """ start the background process"""
    scheduler = BackgroundScheduler()
    trigger = OrTrigger([CronTrigger(hour=9),
                         CronTrigger(hour=10),
                         CronTrigger(hour=13, minute=45),
                         CronTrigger(hour=18),
                         CronTrigger(hour=21)])
    scheduler.add_job(send_email_reminders, trigger)
    scheduler.start()

""" app configuration """
from django.apps import AppConfig


class FlightapiConfig(AppConfig):
    """ Flight api configuration"""
    name = 'flightApi'

    def ready(self):
        from .tasks import start_process
        start_process()

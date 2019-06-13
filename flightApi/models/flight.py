""" Flight model"""

# pylint: disable=too-few-public-methods

from datetimeutc.fields import DateTimeUTCField
from django.conf import settings
from django.db import models


class Flight(models.Model):
    """ Flights model."""

    FLIGHT_CLASS = (
        ('economy', 'Economy'),
        ('business', 'Business'),
        ('first class', 'First Class')
    )

    flight_name = models.CharField(max_length=30)
    flight_class = models.CharField(max_length=20, choices=FLIGHT_CLASS)
    departure_date = DateTimeUTCField(null=False)
    return_date = DateTimeUTCField(null=True)
    departure_airport = models.CharField(max_length=100)
    arriving_airport = models.CharField(max_length=100)
    passenger = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.CASCADE, related_name='passenger')

    class Meta:
        """Define metadata options."""

        ordering = ('pk', )
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

    def __str__(self):
        """Returns object's  string representation"""
        return f'{self.flight_name}'

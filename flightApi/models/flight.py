""" Flight model"""

# pylint: disable=too-few-public-methods

from django.db import models

from flightApi.models.user import User


class Flight(models.Model):
    """ Flights model."""

    FLIGHT_CLASS = (
        ('E', 'Economy'),
        ('B', 'Business'),
        ('F', 'First Class')
    )

    name = models.CharField(max_length=30)
    flight_class = models.CharField(max_length=1, choices=FLIGHT_CLASS)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True)
    departure_airport = models.CharField(max_length=100)
    arriving_airport = models.CharField(max_length=100)
    no_of_passenger = models.PositiveSmallIntegerField()
    passenger = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='flights')

    class Meta:
        """Define metadata options."""

        ordering = ('pk', )
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

    def __str__(self):
        """Returns object's  string representation"""
        return f'{self.name}'

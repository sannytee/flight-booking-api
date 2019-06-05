""""Create your serializers here."""
from rest_framework import serializers

from flightApi.models import User, Flight


# pylint: disable=too-few-public-methods, bad-option-value
class FlightSerializer(serializers.ModelSerializer):
    """
        Flight Model serializer
    """
    # passenger = serializers.StringRelatedField(read_only=True)

    class Meta:
        """Access fields and create returned object"""
        model = Flight
        fields = ('flight_name', 'flight_class', 'departure_date', 'return_date',
                  'departure_airport', 'arriving_airport', 'passenger')


class UserSerializer(serializers.ModelSerializer):
    """
    User Model serializer
    """
    flights = FlightSerializer(many=True, read_only=True)

    class Meta:
        """Access fields and create returned object"""
        model = User
        fields = ('id', 'first_name',
                  'last_name', 'email', 'profile_picture', 'flights'
                  )
        read_only_field = ('first_name', 'last_name', 'email')


class FlightUserSerializer(serializers.ModelSerializer):
    """
        Flight-User serializer
    """
    passenger = serializers.StringRelatedField(read_only=True)

    class Meta:
        """Access fields and create returned object"""
        model = Flight
        fields = ('flight_name', 'flight_class', 'departure_date', 'return_date',
                  'departure_airport', 'arriving_airport', 'passenger')

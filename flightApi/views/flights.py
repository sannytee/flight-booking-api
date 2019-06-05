""" Flights viewset """
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import (HTMLFormRenderer, JSONRenderer,
                                      BrowsableAPIRenderer)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from flightApi.models import Flight
from flightApi.serializers import FlightSerializer
from flightApi.util.helpers import check_user_input, get_flight_and_time, filter_flight_field


# pylint: disable=no-member
class FlightViewset(ViewSet):
    """ Flight viewset"""
    serializer_class = FlightSerializer
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)
    queryset = Flight.objects.all()
    permission_classes = (IsAuthenticated, )

    def create(self, request):
        """ book a flight """
        flight_info = request.data.copy()
        query = request.query_params.get('type')
        required_fields = ['departure_date', 'departure_airport',
                           'flight_class', 'arriving_airport']
        if query == 'round':
            required_fields.append('return_date')
        validate_input = check_user_input(required_fields, flight_info)
        if validate_input:
            data = {
                'status': 'error',
                'error': 'missing field(s)',
                'message': validate_input
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        user = self.request.user
        flight_info['flight_name'], flight_time = get_flight_and_time()
        flight_info['flight_class'] = flight_info['flight_class'].lower()
        flight_info['departure_date'] += ' ' + flight_time
        if query == 'round':
            flight_info['return_date'] += ' ' + flight_time
        flight_info['passenger'] = user.pk
        required_fields += ['flight_name', 'passenger']
        serializers = FlightSerializer(data=filter_flight_field(flight_info, required_fields),
                                       context={'request': request})
        if serializers.is_valid():
            serializers.save()
            data = {
                'status': 'success',
                'message': 'flight successfully booked',
                'flightDetails': filter_flight_field(serializers.data, required_fields[:-1]),
                'booked by': '{} {}'.format(user.first_name, user.last_name)
            }
            return Response(data, status=status.HTTP_201_CREATED)
        data = {
            'status': 'error',
            'error': serializers.errors
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

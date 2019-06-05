"""Admin views"""
from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.renderers import (HTMLFormRenderer, JSONRenderer,
                                      BrowsableAPIRenderer)
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from flightApi.models import Flight, User
from flightApi.serializers import FlightUserSerializer


# pylint: disable=no-member, no-self-use
class AdminOpsViewSet(ViewSet):
    """ Admin viewset"""
    renderer_classes = (JSONRenderer, BrowsableAPIRenderer, HTMLFormRenderer)
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)

    def retrieve_flight_booking(self, request):
        """Get passengers for a particular flight  and specific date"""
        flights = Flight.objects
        queryset = flights.none()
        name = request.query_params.get('name')
        date = request.query_params.get('date')
        if name:
            queryset = flights.filter(
                Q(flight_name__icontains=name)
            )
        elif name and date:
            queryset = flights.filter(
                Q(flight_name__icontains=name) & Q(departure_date=date)
            )
        serializers = FlightUserSerializer(queryset, many=True, context={'request': request})
        passengers = [ticket['passenger'] for ticket in serializers.data]
        passengers_count = len(passengers)
        if passengers_count > 0:
            data = {
                "status": "success",
                "passengers": passengers,
                "message": f'passengers for flight {name.replace(" ", "-")} successfully retrieved'
            }
            return Response(data, status=status.HTTP_200_OK)
        data = {
            "status": "success",
            "message": f'No passengers for the flight {name.replace(" ", "-")}'
        }
        return Response(data, status=status.HTTP_200_OK)

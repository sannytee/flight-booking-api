"""Checks the status of the API"""
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

# pylint: disable=unused-argument, no-self-use

class ApiStatusViewSet(ViewSet):
    """ Status api viewset """
    renderer_classes = (JSONRenderer,)
    permission_classes = (AllowAny,)

    def retrieve(self, request):
        """
        Get the status of the API
        """
        data = {
            "status": "success",
            "message": "Welcome to the Flight API"
        }
        return Response(data, status=status.HTTP_200_OK)

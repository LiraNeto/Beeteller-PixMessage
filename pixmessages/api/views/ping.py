from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def ping(request):
    return Response('pong', status=status.HTTP_200_OK)

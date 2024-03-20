import time

import shortuuid
from django.db import ProgrammingError
from django.utils.timezone import now
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils.serializer_helpers import ReturnDict

from pixmessages.api.caches.ispb_collector import check_ispb_limit, stop_collecting
from pixmessages.api.models import Interaction, get_pix_messages_model
from pixmessages.api.serializers.pix_message_serializer import get_pix_message_serializer

waiting_time = 5


def get_messages(request, ispb):
    my_uuid = shortuuid.random(length=12)
    interaction = Interaction(id=my_uuid, ispb=ispb)
    interaction.save()
    headers = {'Pull-Next': my_uuid}

    qty = 1
    if request.headers.get('Accept') == 'multipart/json':
        qty = 10

    m = get_pix_messages_model(_db_table=ispb)
    messages = m.objects.filter(interationId__isnull=True)[:qty]
    s = get_pix_message_serializer(_db_table=ispb)
    serializer = s(messages, many=True)

    retry = False
    data = ReturnDict
    try:
        data = serializer.data
    except ProgrammingError:
        retry = True

    if retry or not data:
        time.sleep(waiting_time)
        messages = m.objects.filter(interationId__isnull=True)[:qty]
        serializer = s(messages, many=True)
        try:
            data = serializer.data
        except ProgrammingError:
            return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)
        if not data:
            return Response(status=status.HTTP_204_NO_CONTENT, headers=headers)
    m.objects.filter(id__in=messages).update(interationId=my_uuid)
    return Response(data=data, status=status.HTTP_200_OK, headers=headers)


@api_view(['GET'])
def start(request, ispb):
    if not check_ispb_limit(ispb):
        return Response(status=status.HTTP_429_TOO_MANY_REQUESTS)
    return get_messages(request, ispb)


@api_view(['GET', 'DELETE'])
def read(request, ispb, interation_id):
    try:
        i = Interaction.objects.get(id=interation_id, ispb=ispb, date_used__isnull=True)
    except Interaction.DoesNotExist:
        data = {'Error': "InteractionID not found or already used", 'InterationID': interation_id, 'ISPB': ispb}
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    i.date_used = now()
    i.save()

    match request.method:
        case 'GET':
            return get_messages(request, ispb)
        case 'DELETE':
            stop_collecting(ispb)
            return Response(data={}, status=status.HTTP_200_OK)
        case _:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

from rest_framework import serializers

from api.models import get_pix_messages_model, Person
from api.serializers.person_serializer import PersonSerializer


def get_pix_message_serializer(_db_table):
    dinamic_model = get_pix_messages_model(_db_table=_db_table)

    class PixMessageSerializer(serializers.ModelSerializer):
        recebedor = PersonSerializer()
        pagador = PersonSerializer()
        campoLivre = serializers.CharField(
            max_length=250, allow_blank=True
        )

        class Meta:
            model = dinamic_model
            fields = ['endToEndId', 'valor', 'campoLivre', 'txId', 'dataHoraPagamento', 'recebedor', 'pagador']

        def create(self, validated_data):
            recebedor_data = validated_data.pop('recebedor')
            recebedor, _ = Person.objects.get_or_create(**recebedor_data)
            pagador_data = validated_data.pop('pagador')
            pagador, _ = Person.objects.get_or_create(**pagador_data)
            pix_message = dinamic_model.objects.create(pagador=pagador, recebedor=recebedor, **validated_data)
            return pix_message

    return PixMessageSerializer

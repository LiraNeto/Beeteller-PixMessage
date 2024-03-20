from rest_framework import serializers

from api.models.PersonModel import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['nome', 'cpfCnpj', 'ispb', 'agencia', 'contaTransacional', 'tipoConta']

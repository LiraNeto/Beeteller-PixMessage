from django.db import models
from django.db.models.base import ModelBase

from .person_model import Person


def get_pix_messages_model(_db_table):
    _db_table = f'api_pixmessage_{_db_table}'

    class MyClassMetaclass(ModelBase):
        def __new__(cls, name, bases, attrs):
            name += _db_table
            return models.base.ModelBase.__new__(cls, name, bases, attrs)

    class PixMessages(models.Model):
        __metaclass__ = MyClassMetaclass
        endToEndId = models.CharField(max_length=250)
        valor = models.DecimalField(decimal_places=2, max_digits=10)
        campoLivre = models.TextField()
        txId = models.CharField(max_length=250)
        dataHoraPagamento = models.DateTimeField()
        recebedor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='recebedor_pixmessage_set')
        pagador = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='pagador_pixmessage_set')
        interationId = models.CharField(null=True, max_length=12)

        class Meta:
            db_table = _db_table

    return PixMessages



from django.db import models


class Person(models.Model):
    nome = models.CharField(max_length=250)
    cpfCnpj = models.CharField(max_length=14)
    ispb = models.CharField(max_length=8)
    agencia = models.CharField(max_length=10)
    contaTransacional = models.CharField(max_length=20)
    tipoConta = models.CharField(max_length=4)

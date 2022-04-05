from django.db import models
from rest_framework import serializers
class Setor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=1000, null=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = ('id', 'nome', 'descricao', 'ativo')
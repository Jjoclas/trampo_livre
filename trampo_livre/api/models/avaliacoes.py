from django.db import models
from rest_framework import serializers


class Avaliacoes(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=1000, null=False)
    atividade = models.ForeignKey('Atividades', on_delete=models.CASCADE)
    nota = models.IntegerField(null=False)

    def __str__(self):
        return self.titulo

class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        fields = ('id', 'titulo', 'descricao', 'atividade', 'nota')
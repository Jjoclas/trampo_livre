from django.db import models
from rest_framework import serializers
from enum import Enum

class RepeticaoTypes(Enum):
  diaria = 'diaria'
  dia_util = 'dias uteis'
  semanal = 'semanal'
  mensal = 'mensal'
  nunca = 'nunca'
  
  @classmethod
  def choices(cls):
    return [(key.value, key.name) for key in cls]

class Agenda(models.Model):
    atividade = models.ForeignKey('Atividades', on_delete=models.CASCADE)
    data_inicio = models.DateTimeField(null=False)
    data_fim = models.DateTimeField()
    repeticao = models.CharField(max_length=10, choices=RepeticaoTypes.choices())
    hora_inicio = models.TimeField(null=True)
    hora_fim = models.TimeField(null=True)

    def __str__(self):
        return self.atividade.titulo

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'
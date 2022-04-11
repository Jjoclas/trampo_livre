from django.db import models
from rest_framework import serializers

class Atividades(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=1000, null=False)
    profissional = models.ForeignKey('Profissionais', on_delete=models.CASCADE)
    contratante = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    horas_realizadas = models.IntegerField(null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class AtividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividades
        fields = '__all__'
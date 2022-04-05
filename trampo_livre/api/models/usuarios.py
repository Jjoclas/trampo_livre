import uuid
from django.db import models
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class Usuarios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    senha = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class UsuariosSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)
    class Meta:
        model = Usuarios
        fields = ('id', 'nome', 'senha', 'email', 'telefone', 'data_cadastro', 'data_atualizacao', 'ativo')

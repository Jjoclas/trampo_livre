from django.db import models

class Atividades(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=1000, null=False)
    data_incio = models.DateTimeField(null=False)
    data_fim = models.DateTimeField(null=False)
    setor = models.ForeignKey('Setor', on_delete=models.CASCADE)
    profisional = models.ForeignKey('Profissionais', on_delete=models.CASCADE)
    contratante = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    avaliacao = models.ForeignKey('Avaliacoes', on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    horas_realizadas = models.IntegerField(null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
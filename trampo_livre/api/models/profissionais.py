from django.db import models

class Profissionais(models.Model):
    usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=1000, null=False)
    valor_hora = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)
    cpf = models.CharField(max_length=11, null=False)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    setor = models.ForeignKey('Setor', on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.nome
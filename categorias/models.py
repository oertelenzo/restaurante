from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=60)
    descricao = models.TextField()
    ativa = models.BooleanField(default=True)
    criada_em = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

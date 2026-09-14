from django.db import models

from categorias.models import Categoria


class Prato(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    tempo_preparo_min = models.IntegerField()
    vegetariano = models.BooleanField(default=False)

    # Relacionamento 1:N com Categoria.
    # Uma categoria (ex: "Massas") tem varios pratos, mas cada prato
    # pertence a apenas uma categoria. Por isso a ForeignKey fica aqui,
    # no lado "muitos". Se a categoria for apagada, os pratos dela
    # tambem sao apagados (CASCADE).
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

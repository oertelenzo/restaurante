from django.db import models


class Mesa(models.Model):
    # campo com valores fixos, entao usamos choices
    LOCALIZACAO_CHOICES = [
        ("salao", "Salao interno"),
        ("varanda", "Varanda"),
        ("externa", "Area externa"),
    ]

    numero = models.IntegerField()
    capacidade = models.IntegerField()
    localizacao = models.CharField(max_length=20, choices=LOCALIZACAO_CHOICES)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return "Mesa " + str(self.numero)

from django.db import models

from datetime import datetime

OPCOES_CATEGORIA = [
    ("NEBULOSA", "Nebulosa"),
    ("ESTRELA", "Estrela"),
    ("GALÁXIA", "Galáxia"),
    ("PLANETA", "Planeta"),
]


class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=100, null=False, blank=False)
    data_fotografia = models.DateTimeField(default=datetime.now(), blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return f"Fotografia : {self.nome}"

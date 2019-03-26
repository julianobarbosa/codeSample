from django.db import models


class Artista(models.Model):
    nome = models.CharField('nome', max_length=100)

    class Meta:
        verbose_name = 'artista'
        verbose_name_plural = 'artistas'
        ordering = ('nome', )

    def __str__(self):
        return self.nome
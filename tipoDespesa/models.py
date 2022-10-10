from django.db import models


class TipoDespesa(models.Model):
    nome = models.CharField('Tipo Despesa', max_length=50)
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Tipo Despesa'
        verbose_name_plural = 'Tipos Despesas'
        ordering = ['nome']

    def __str__(self):
        return self.nome


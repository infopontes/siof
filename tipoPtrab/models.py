from django.db import models


class TipoPtrab(models.Model):
    nome = models.CharField('Tipo PTrab', max_length=50)
    descricao = models.CharField('Descrição', max_length=100)
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Tipo PTrab'
        verbose_name_plural = 'Tipos PTrab'
        ordering = ['nome']

    def __str__(self):
        return self.nome

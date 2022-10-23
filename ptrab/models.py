from django.db import models

from documento.models import Documento
from tipoPtrab.models import TipoPtrab


class Ptrab(models.Model):
    numero = models.IntegerField('Número')
    data = models.DateField('Data', auto_now=True)
    tipo_ptrab_id = models.ForeignKey(TipoPtrab, on_delete=models.CASCADE, verbose_name='Tipo')
    operacao = models.CharField('Operação', max_length=100)
    acao = models.CharField('Ação', max_length=200)
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)
    documento_id = models.ForeignKey(Documento, on_delete=models.CASCADE, verbose_name='Documento')

    class Meta:
        verbose_name = 'PTrab'
        verbose_name_plural = 'PTrab'
        ordering = ['numero']

    def __str__(self):
        return str(self.numero) + "-" + self.operacao

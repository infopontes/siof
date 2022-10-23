from django.db import models

from unidade.models import Unidade


class Documento(models.Model):
    numero = models.IntegerField(verbose_name='Nr Documento')
    data = models.DateField(verbose_name='Data')    
    om = models.ForeignKey(Unidade, on_delete=models.CASCADE, verbose_name='OM')
    secao = models.CharField(verbose_name='Seção', max_length=50)
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Documentos'
        verbose_name_plural = 'Documentos'
        ordering = ['numero']

    def __str__(self):
        return str(self.numero) + ' - ' + self.secao

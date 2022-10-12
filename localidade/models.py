from django.db import models

from despesa.models import Despesa


class Estado(models.Model):
    codigo = models.IntegerField(primary_key=True)
    uf = models.CharField('UF', max_length=2)
    nome = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField('Nome', max_length=50)
    estado_id = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name='Estado')

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Localidade(models.Model):
    cidade_id = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name='Cidade')
    despesa_id = models.ForeignKey(Despesa, on_delete=models.CASCADE, verbose_name='Despesa')
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Localidade'
        verbose_name_plural = 'Localidades'

    def __str__(self):
        return self.cidade_id__nome



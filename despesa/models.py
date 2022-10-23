from django.db import models

from ptrab.models import Ptrab
from tipoDespesa.models import TipoDespesa
from unidade.models import Unidade


class Despesa(models.Model):
    ND_15 = 15
    ND_30 = 30
    ND_33 = 33
    ND_39 = 39
    ND_40 = 40
    ND_52 = 52

    ND_CHOICES = (
        (ND_15, '33.90.15'),
        (ND_30, '33.90.30'),
        (ND_33, '33.90.33'),
        (ND_39, '33.90.39'),
        (ND_40, '44.90.40'),
        (ND_52, '44.90.52'),
    )

    tipo_despesa_id = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE, verbose_name='Tipo')
    unidade_id = models.ForeignKey(Unidade, on_delete=models.CASCADE, verbose_name='Unidade')
    nd = models.CharField(max_length=5, choices=ND_CHOICES, blank=False, null=False, verbose_name='ND')
    valor = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name='Valor (R$)')
    memoria_calculo = models.TextField('Memória Cálculo')
    ptrab_id = models.ForeignKey(Ptrab, on_delete=models.CASCADE, verbose_name='PTrab')
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)


    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        ordering = ['unidade_id']

    def __str__(self):
        return self.tipo_despesa_id.nome




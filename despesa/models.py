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
        (ND_15, 339015),
        (ND_30, 339030),
        (ND_33, 339033),
        (ND_39, 339039),
        (ND_40, 449040),
        (ND_52, 449052),
    )

    tipo_despesa_id = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE, verbose_name='Tipo Despesa')
    unidade_id = models.ForeignKey(Unidade, on_delete=models.CASCADE, verbose_name='Unidade')
    data = models.DateField('Data', auto_now=True)
    nd = models.CharField(max_length=5, choices=ND_CHOICES, blank=False, null=False, verbose_name='ND')
    valor = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name='Valor (R$)')
    memoria_calculo = models.TextField('Memória Cálculo')
    ptrab_id = models.ForeignKey(Ptrab, on_delete=models.CASCADE, verbose_name='PTrab')
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)


    class Meta:
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'
        ordering = ['data']

    def __str__(self):
        return self.tipo_despesa_id.nome




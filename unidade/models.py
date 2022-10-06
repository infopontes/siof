from django.db import models


RM_CHOICE=(
        (1, '1ª RM'),
        (2, '2ª RM'),
        (3, '3ª RM'),
        (4, '4ª RM'),
        (5, '5ª RM'),
        (6, '6ª RM'),
        (7, '7ª RM'),
        (8, '8ª RM'),
        (9, '9ª RM'),
        (10, '10ª RM'),
        (11, '11ª RM'),
        (12, '12ª RM'),
    )

CMILA_CHOICE=(
        (1, 'CMA'),
        (2, 'CMN'),
        (3, 'CMNE'),
        (4, 'CMSE'),
        (5, 'CML'),
        (6, 'CMS'),
        (7, 'CMO'),
        (8, 'CMP'),
    )


class Unidade(models.Model):
    """
    Esta classe é responsável pelo cadastro das informações das Organizações Militares (OM) do Exército.
    """
    
    codug = models.CharField(verbose_name='CODUG', max_length=7, help_text='Digite o codug da OM, por exemplo: 160539')
    autonomia = models.BooleanField(verbose_name='Autonomia', help_text='Marque se a OM tem autonomia administrativa')
    nome = models.CharField(verbose_name='Nome OM', max_length=50, help_text='Digite o nome da OM, por exemplo: Comando de Operações Terrestres')
    rm = models.IntegerField(verbose_name='RM', choices=RM_CHOICE)
    c_mil_a = models.IntegerField(verbose_name='C Mil A', choices=CMILA_CHOICE)
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)


    def __str__(self):
        return self.nome + ' - ' + CMILA_CHOICE[self.c_mil_a -1][1] + ' - ' + RM_CHOICE[self.rm -1][1]

from django.db import models


class ComandoMilitarArea(models.Model):
    abreviatura = models.CharField(verbose_name='Abreviatura', max_length=5)
    nome = models.CharField(verbose_name='C Mil A', max_length=50)
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)
    class Meta:
        verbose_name = 'C Mil A'
        verbose_name_plural = 'C Mil A'
        ordering = ['abreviatura']

    def __str__(self):
        return self.abreviatura + ' - ' + self.nome


class RegiaoMilitar(models.Model):
    abreviatura = models.CharField(verbose_name='Abreviatura', max_length=10)
    nome = models.CharField(verbose_name='RM', max_length=50)
    c_mil_a = models.ForeignKey(ComandoMilitarArea, on_delete=models.CASCADE, verbose_name='C Mil A')
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'RM'
        verbose_name_plural = 'RM'
        ordering = ['abreviatura']

    def __str__(self):
        return self.abreviatura + ' - ' + self.nome


class Unidade(models.Model):
    """
    Esta classe é responsável pelo cadastro das informações das Organizações Militares (OM) do Exército.
    """
    codug = models.CharField(verbose_name='CODUG', max_length=7, help_text='Digite o codug da OM, por exemplo: 160539')
    autonomia = models.BooleanField(verbose_name='Autonomia', help_text='Marque se a OM tem autonomia administrativa')
    nome = models.CharField(verbose_name='Nome OM', max_length=50, help_text='Digite o nome da OM, por exemplo: Comando de Operações Terrestres')
    rm = models.ForeignKey(RegiaoMilitar, on_delete=models.CASCADE, verbose_name='RM')
    criado_em = models.DateTimeField(verbose_name='Criado em', auto_now_add=True)
    atualizado_em = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ['codug']


    def __str__(self):
        return self.codug + ' - ' + self.nome

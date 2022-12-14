# Generated by Django 4.1.1 on 2022-10-10 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ptrab', '0001_initial'),
        ('tipoDespesa', '0001_initial'),
        ('unidade', '0004_alter_comandomilitararea_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True, verbose_name='Data')),
                ('nd', models.CharField(choices=[(15, 339015), (30, 339030), (33, 339033), (39, 339039), (40, 449040), (52, 449052)], max_length=5, verbose_name='ND')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor (R$)')),
                ('memoria_calculo', models.TextField(verbose_name='Memória Cálculo')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('ptrab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptrab.ptrab', verbose_name='PTrab')),
                ('tipo_despesa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipoDespesa.tipodespesa', verbose_name='Tipo Despesa')),
                ('unidade_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='unidade.unidade', verbose_name='Unidade')),
            ],
            options={
                'verbose_name': 'Despesa',
                'verbose_name_plural': 'Despesas',
                'ordering': ['data'],
            },
        ),
    ]

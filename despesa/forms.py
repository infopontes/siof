from cProfile import label
from select import select
from unicodedata import name
from django.forms import ModelForm, Textarea, DecimalField

from .models import Despesa


class DespesaForm(ModelForm):
    required_css_class = 'required'
    valor = DecimalField(max_digits=8, decimal_places=2, localize=True)
    class Meta:
        model = Despesa
        fields = ('ptrab_id','tipo_despesa_id', 'unidade_id', 'nd','valor', 'memoria_calculo')
        widgets = {
            'memoria_calculo': Textarea(attrs={'placeholder': 'Memória de Cálculo','cols': 25, 'rows': 1}),
        }
    
        
    def __init__(self, *args, **kwargs):
        super(DespesaForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        self.fields['valor'].localize = True
        self.fields['valor'].widget.is_localized = True
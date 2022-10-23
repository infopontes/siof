from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import DespesaForm
from .models import Despesa

def despesa_list(request):
    template_name = 'despesa/despesa_list.html'
    form = DespesaForm(request.POST or None)

    despesas = Despesa.objects.all()

    context = {'object_list': despesas, 'form': form}
    return render(request, template_name, context)
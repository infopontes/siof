from django.shortcuts import render

def unidade_list(request):
    template_name = 'unidade/unidade_list.html'
    return render(request, template_name)
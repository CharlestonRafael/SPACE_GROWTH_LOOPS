from django.shortcuts import render

from my_growth_loop.models import Ideias

def index(request):
    return render(request, 'my_growth_loop/index.html')

def awareness(request):
    return render(request, 'my_growth_loop/awareness.html')

def aquisicao(request):
    return render(request, 'my_growth_loop/aquisicao.html')

def ativacao(request):
    return render(request, 'my_growth_loop/ativacao.html')

def retencao(request):
    return render(request, 'my_growth_loop/retencao.html')

def receita(request):
    return render(request, 'my_growth_loop/receita.html')

def referral(request):
    return render(request, 'my_growth_loop/referral.html')

def ideias(request):
    Ideias = Ideias.objects.all()
    return render(request, 'my_growth_loop/ideias.html')

def growth_plan(request):
    return render(request, 'my_growth_loop/growth_plan.html')

def integracoes(request):
    return render(request, 'my_growth_loop/integracoes.html')

def usuarios(request):
    return render(request, 'my_growth_loop/usuarios.html')

def investimento(request):
    return render(request, 'my_growth_loop/investimento.html')

def meu_perfil(request):
    return render(request, 'my_growth_loop/meu_perfil.html')





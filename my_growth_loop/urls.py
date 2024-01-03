from django.urls import path
from my_growth_loop.views import index, awareness, aquisicao, ativacao, retencao, receita, referral, ideias, growth_plan, integracoes, usuarios, investimento, meu_perfil

urlpatterns = [
    path('', index, name='index'),
    path('awareness/', awareness, name='awareness'),
    path('aquisicao/', aquisicao, name='aquisicao'),
    path('ativacao/', ativacao, name='ativacao'),
    path('retencao/', retencao, name='retencao'),
    path('receita/', receita, name='receita'),
    path('referral/', referral, name='referral'),
    path('ideias/', ideias, name='ideias'),
    path('growth_plan/', growth_plan, name='growth_plan'),
    path('integracoes/', integracoes, name='integracoes'),
    path('usuarios/', usuarios, name='usuarios'),
    path('investimento/', investimento, name='investimento'),
    path('meu_perfil/', meu_perfil, name='meu_perfil'),
]
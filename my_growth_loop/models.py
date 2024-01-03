from django.db import models

from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator

class Ideias(models.Model):

    OPCOES_ETAPA = [
        ("AWARENESS", "Awareness"),
        ("AQUISIÇÃO", "Aquisição"),
        ("ATIVAÇÃO", "Ativação"),
        ("RETENÇÃO", "Retenção"),
        ("RECEITA", "Receita"),
        ("RECOMENDAÇÃO", "Recomendação"),
    ]
    
    OPCOES_METRICAS = [
        ("CTR", "CTR"),
        ("TAXA DE CONVERSÃO LEADS X VISITAS", "Taxa de Conversão Leads x Visitas"),
        ("TAXA DE CONVERSÃO OPORTUNIDADES X LEADS", "Taxa de conversão Oportunidades x Leads"),
        ("TAXA DE CONVERSÃO VENDAS X OPORTUNIDADES", "Taxa de COnversão Vendas x Oportunidades"),
        ("CHURN RATE", "Churn Rate"),
        ("TAXA DE ENGAJAMENTO", "Taxa de Engajamento"),
        ("CAC", "CAC"),
    ]

    OPCOES_GATILHO = [
        ("ACIMA DA MÉDIA", "Acima da Média"),
        ("ABAIXO DA MÉDIA", "Abaixo da Média"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    etapa = models.CharField(max_length=100, choices=OPCOES_ETAPA, default='')
    metrica = models.CharField(max_length=100, choices=OPCOES_METRICAS, default='')
    gatilho = models.CharField(max_length=100, choices=OPCOES_GATILHO, default='')
    publicada =models.BooleanField(default=False)
    data_ideia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"Ideias [nome={self.nome}]"

class Metricas(models.Model):
    nome_metrica = models.CharField(max_length=100, null=False, blank=False)
    valor_metrica = models.FloatField(max_length=100, null=False, blank=False)                         
    data_medicao = models.DateTimeField(default=datetime.now, blank=False)
                                    
    def __str__(self):
        return f"Metricas [nome={self.nome}]"

class Parametro(models.Model):

    OPCOES_METRICA_PARAMETRO = [
        ("CTR MÉDIA", "CTR Média"),
        ("CTR GOOGLE ADS", "CTR Google Ads"),
        ("CTR META ADS", "CTR Meta Ads"),
        ("CTR LINKEDIN ADS", "CTR Linkedin Ads"),
        ("CTR TIKTOK ADS", "CTR TikTok Ads"),
        ("TAXA DE CONVERSÃO LEADS X VISITAS", "Taxa de Conversão Leads x Visitas"),
        ("TAXA DE CONVERSÃO OPORTUNIDADES X LEADS", "Taxa de conversão Oportunidades x Leads"),
        ("TAXA DE CONVERSÃO VENDAS X OPORTUNIDADES", "Taxa de COnversão Vendas x Oportunidades"),
        ("CHURN RATE", "Churn Rate"),
        ("TAXA DE ENGAJAMENTO", "Taxa de Engajamento"),
        ("CAC", "CAC"),
        ("CAC X LTV", "CAC X LTV"),
        ("NPS", "NPS"),
    ]

    nome_metrica_parametro = models.CharField(max_length=100, choices= OPCOES_METRICA_PARAMETRO, default='')
    valor_metrica_parametro = models.FloatField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Parametro [nome={self.nome}]"

                                    
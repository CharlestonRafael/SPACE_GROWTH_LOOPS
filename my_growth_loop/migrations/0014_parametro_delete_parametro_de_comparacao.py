# Generated by Django 4.2.5 on 2024-01-01 22:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_growth_loop', '0013_parametro_de_comparacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_metrica_parametro', models.CharField(choices=[('CTR MÉDIA', 'CTR Média'), ('CTR GOOGLE ADS', 'CTR Google Ads'), ('CTR META ADS', 'CTR Meta Ads'), ('CTR LINKEDIN ADS', 'CTR Linkedin Ads'), ('CTR TIKTOK ADS', 'CTR TikTok Ads'), ('TAXA DE CONVERSÃO LEADS X VISITAS', 'Taxa de Conversão Leads x Visitas'), ('TAXA DE CONVERSÃO OPORTUNIDADES X LEADS', 'Taxa de conversão Oportunidades x Leads'), ('TAXA DE CONVERSÃO VENDAS X OPORTUNIDADES', 'Taxa de COnversão Vendas x Oportunidades'), ('CHURN RATE', 'Churn Rate'), ('TAXA DE ENGAJAMENTO', 'Taxa de Engajamento'), ('CAC', 'CAC'), ('CAC X LTV', 'CAC X LTV'), ('NPS', 'NPS')], default='', max_length=100)),
                ('valor_metrica_parametro', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
            ],
        ),
        migrations.DeleteModel(
            name='Parametro_de_Comparacao',
        ),
    ]

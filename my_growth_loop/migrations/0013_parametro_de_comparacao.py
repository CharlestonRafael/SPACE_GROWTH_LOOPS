# Generated by Django 5.0 on 2023-12-31 20:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_growth_loop', '0012_rename_data_metricas_data_medicao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametro_de_Comparacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_metrica_parametro', models.CharField(max_length=100)),
                ('valor_metrica_parametro', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
            ],
        ),
    ]

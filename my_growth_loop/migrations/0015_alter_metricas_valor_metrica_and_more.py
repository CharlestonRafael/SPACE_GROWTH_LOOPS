# Generated by Django 4.2.5 on 2024-01-01 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_growth_loop', '0014_parametro_delete_parametro_de_comparacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricas',
            name='valor_metrica',
            field=models.FloatField(max_length=100),
        ),
        migrations.AlterField(
            model_name='parametro',
            name='valor_metrica_parametro',
            field=models.FloatField(max_length=100),
        ),
    ]

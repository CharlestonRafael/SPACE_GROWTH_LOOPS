# Generated by Django 4.2.5 on 2024-01-01 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_growth_loop', '0016_alter_metricas_valor_metrica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metricas',
            name='valor_metrica',
            field=models.FloatField(max_length=100),
        ),
    ]

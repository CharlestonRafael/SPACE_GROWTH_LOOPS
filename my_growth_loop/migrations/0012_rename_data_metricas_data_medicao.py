# Generated by Django 4.2.5 on 2023-12-30 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_growth_loop', '0011_metricas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metricas',
            old_name='data',
            new_name='data_medicao',
        ),
    ]

# Generated by Django 4.2.5 on 2023-12-29 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_growth_loop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repositorioideias',
            old_name='Descricao',
            new_name='descricao',
        ),
    ]

from django.contrib import admin

from my_growth_loop.models import Ideias

from my_growth_loop.models import Metricas

from my_growth_loop.models import Parametro

class ListandoIdeias(admin.ModelAdmin):
    list_display = ("id", "nome", "descricao", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome" ,)
    list_filter = ("etapa" ,)
    list_editable: ("publicada" ,)
    list_per_page = 10

admin.site.register(Ideias, ListandoIdeias)

class ListandoMetricas(admin.ModelAdmin):
    list_display = ("id", "nome_metrica", "valor_metrica")
    list_display_links = ("id", "nome_metrica")
    search_fields = ("nome_metrica" ,)
    list_per_page = 10
admin.site.register(Metricas, ListandoMetricas)

class ListandoParametro(admin.ModelAdmin):
    list_display = ("id", "nome_metrica_parametro", "valor_metrica_parametro")
    list_display_links = ("id", "nome_metrica_parametro")
    search_fields = ("nome_metrica_parametro" ,)
    list_filter = ("nome_metrica_parametro" ,)
    list_per_page = 10
admin.site.register(Parametro, ListandoParametro)

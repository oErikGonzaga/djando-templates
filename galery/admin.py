from django.contrib import admin

from galery.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display = "id", "nome", "legenda"
    list_display_links = "nome",
    search_fields = "nome",
    ordering = "id",


admin.site.register(Fotografia, ListandoFotografias)

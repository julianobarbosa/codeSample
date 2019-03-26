from django.contrib import admin
from codesample.albums.models import Artista


class ArtistaModelAdmin(admin.ModelAdmin):
    list_display = ('nome', )
    search_fields = ('nome', )

admin.site.register(Artista, ArtistaModelAdmin)
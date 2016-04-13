from django.contrib import admin

from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

from .models import (Taxon, Rank, ScientificName)

class RankAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ('__str__',)

class TaxonAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ('__str__',)

    class Meta:
        verbose_name_plural = "Taxa"

class ScientificNameAdmin(admin.ModelAdmin):

   def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "genus":
            kwargs["queryset"] = Taxon.objects.filter(rank="Genus")
        return super(ScientificNameAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Taxon, TaxonAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(ScientificName, ScientificNameAdmin)


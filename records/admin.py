from django.contrib import admin

from .models import (Crop, 
        Site, 
        BedSet, 
        Block
        )

class CropAdmin(admin.ModelAdmin):
    pass

class SiteAdmin(admin.ModelAdmin):
    ordering = ('name',)

admin.site.register(Crop, CropAdmin)
admin.site.register(Site, SiteAdmin)

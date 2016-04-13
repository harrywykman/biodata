from django.db import models

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Rank(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', 
            null=True, 
            blank=True, 
            related_name='children', 
            db_index=True, 
            )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

class Taxon(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    rank = TreeForeignKey('Rank', 
            null=True, 
            blank=True, 
            related_name='rank', 
            db_index=True
            )
    parent = TreeForeignKey('self', 
            null=True, 
            blank=True, 
            related_name='subtaxa', 
            db_index=True, 
            verbose_name="supertaxon"
            )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        if self.name:
            return "{}".format(self.name)
        else:
            return ""

class ScientificName(models.Model):
    genus_name = models.ForeignKey('Taxon', null=True, related_name='subgenus')
    specific_epithet = models.ForeignKey('Taxon', null=True, related_name='subspecific')
    subspecific_epithet = models.ForeignKey('Taxon', null=True, blank=True, related_name='subsubspecific')

    def __str__(self):                                                                             
        return "{} {} {}".format(self.genus_name, self.specific_epithet, self.subspecific_epithet)

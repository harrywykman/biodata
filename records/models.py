from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from biota.models import ScientificName

class Location(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=200, null=True)

    class Meta:
        abstract = True


class Input(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=200, null=True)

    class Meta:
        abstract = True

## LOCATION CLASSES ##

class Site(Location):
    pass

class Bed(Location):
    pass

class BedSet(Location):
    site = models.ForeignKey(Site, null=True, blank=True)
    beds = models.ManyToManyField(Bed)

class Block(models.Model):
    user = models.ForeignKey(User, null=True)
    beds = models.ForeignKey(BedSet, null=True)


## INPUTS ##

class Seed(Input):
    packet_name = models.CharField(max_length=100, null=True)

## CROP RECORD CLASSES ##

class CropGroup(models.Model):
    name = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name

class CropVariety(models.Model):
    user = models.ForeignKey(User, null=True)
    crop_group = models.ForeignKey(CropGroup, null=True)
    scientific_name = models.ForeignKey(ScientificName, null=True)
    varieties = models.ManyToManyField(Seed)

class Crop(models.Model):
    user = models.ForeignKey(User, null=True)
    seed = models.ForeignKey(Seed, null=True)


class CropRecord(models.Model):
    user = models.ForeignKey(User, null=True)
    crop = models.ForeignKey(Crop, null=True)
    start_date = models.DateField(
                                   'date of propagation for production',
                                   null=True,
                                   default=timezone.now
                                   )

    class Meta:
        abstract = True

class NurseryRecord(CropRecord):
    pass

class SeederRecord(models.Model):
    user = models.ForeignKey(User, null=True)
    EARTHWAY = 'EW'
    GLASSER = 'GL'
    JANG = 'JANG'
    SEEDER_CHOICES = (
        (EARTHWAY, 'Earthway'),
        (GLASSER, 'Glasser'),
        (JANG, 'Jang'),
    )
    name = models.CharField(max_length=2, choices=SEEDER_CHOICES)
    seeder_settings = models.CharField(max_length=100, null=True)

class BedRecord(CropRecord):
    nursery_record = models.ForeignKey(NurseryRecord, null=True)
    seeder_record = models.ForeignKey(SeederRecord, null=True)
    bed_set = models.ForeignKey(BedSet, null=True)

class HarvestRecord(CropRecord):
    bed_set = models.ForeignKey(BedSet)

class Product(models.Model):
    crops = models.ManyToManyField(Crop)

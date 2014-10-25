from django.db import models
from django.conf import settings
  
class Asset(models.Model):
    UID = models.CharField(max_length=255, unique=True, null=False) # This is the PK
    organizationalTag = models.CharField(max_length=255, blank=False, null=False)
    manufacturerPartNumber = models.CharField(max_length=255, blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=False)
    maintenanceNotes = models.CharField(max_length=255, blank=True, null=False)
    dateImplemented = models.DateField(auto_now=False, auto_now_add=True)
    currentAssignedLocation = models.ForeignKey('Location') #FK to a Location object
    manufacturer = models.ForeignKey('Manufacturer') #FK to a Manufacturer object
    
class Manufacturer(models.Model):
    UID = models.CharField(max_length=255, unique=True, null=False) # This is the PK
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=255, blank=False, null=False)
    
class Location(models.Model):
    UID = models.CharField(max_length=255, unique=True, null=False) # This is the PK
    name = models.CharField(max_length=255, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    phone = models.CharField(max_length=255, blank=False, null=False)
from django.db import models
from django.core.validators import MaxValueValidator


class BaseResults(models.Model):
    result_id = models.AutoField(primary_key=True)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.GenericIPAddressField(max_length=50)

    class Meta:
        abstract = True


class AgentName(models.Model):
    name_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=13)
    pollingunit_uniqueid = models.PositiveIntegerField()

    class Meta:
        db_table = "agentname"


class AnnouncedLGAResults(BaseResults):
    lga_name = models.CharField(max_length=50)
    
    class Meta:
        db_table = "announced_lga_results"


class AnnouncedPollingUnitResults(BaseResults):
    polling_unit_uniqueid = models.CharField(max_length=50)

    class Meta:
        db_table = "announced_pu_results"


class AnnouncedStateResults(BaseResults):
    state_name = models.CharField(max_length=50)

    class Meta:
        db_table = "announced_state_results"


class AnnouncedWardResults(BaseResults):
    ward_name = models.CharField(max_length=50)

    class Meta:
        db_table = "announced_ward_results"



class LGA(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    lga_id = models.PositiveIntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.PositiveIntegerField(validators=[MaxValueValidator(50)])
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.GenericIPAddressField(max_length=50)

    class Meta:
        db_table = "lga"


class Party(models.Model):
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    class Meta:
        db_table = "party"
    

class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    polling_unit_id = models.PositiveIntegerField()
    ward_id = models.PositiveIntegerField()
    lga_id = models.PositiveIntegerField()
    uniquewardid = models.PositiveIntegerField(blank=True, null=True)
    polling_unit_number = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_name = models.CharField(max_length=50, blank=True, null=True)
    polling_unit_description = models.TextField()
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.GenericIPAddressField()

    class Meta:
        db_table = "polling_unit"


class States(models.Model):
    state_id = models.PositiveIntegerField(primary_key=True)
    state_name = models.CharField(max_length=50)

    class Meta:
        db_table = "states"


class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True)
    ward_id = models.PositiveIntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.PositiveIntegerField()
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField(auto_now_add=True)
    user_ip_address = models.GenericIPAddressField()

    class Meta:
        db_table = "ward"
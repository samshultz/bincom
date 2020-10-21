from django import forms
from .models import AnnouncedPollingUnitResults,LGA, PollingUnit, Party, AgentName

POLLING_UNITS_ID = AnnouncedPollingUnitResults.objects.values_list("polling_unit_uniqueid", flat=True).distinct()
POLLING_UNITS_ID = [(i, f"Polling Unit {i}") for i in POLLING_UNITS_ID]

LGA_ID = LGA.objects.values_list("lga_id", "lga_name").distinct()
POLITICAL_PARTIES = [(name, name) for name in Party.objects.values_list("partyname", flat=True)]


class FilterByPollingUnitIdForm(forms.Form):
    polling_unit_id = forms.TypedChoiceField(choices=POLLING_UNITS_ID, coerce=int, required=True)


class LocalGovtSelectionForm(forms.Form):
    lga_id = forms.TypedChoiceField(choices=LGA_ID, coerce=int, required=True)


class PollingUnitForm(forms.ModelForm):
    class Meta:
        model = PollingUnit
        fields = "__all__"

class AgentForm(forms.ModelForm):
    class Meta:
        model = AgentName
        fields = "__all__"

class PartyForm(forms.ModelForm):
    party_abbreviation = forms.ChoiceField(choices=POLITICAL_PARTIES)
    class Meta:
        model = AnnouncedPollingUnitResults
        fields = "__all__"


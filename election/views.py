from django.shortcuts import render
from django.db.models import Sum
from .models import AnnouncedPollingUnitResults, PollingUnit, Party
from .forms import (FilterByPollingUnitIdForm, LocalGovtSelectionForm,
PollingUnitForm, AgentForm, PartyForm)
from django.forms import formset_factory


def display_polling_unit_results(request):
    pu_results = AnnouncedPollingUnitResults.objects.all()
    pu_form = FilterByPollingUnitIdForm()

    if "polling_unit_id" in request.GET:
        pu_form = FilterByPollingUnitIdForm(request.GET)
        if pu_form.is_valid():
            polling_unit_id = pu_form.cleaned_data['polling_unit_id']
            pu_results = AnnouncedPollingUnitResults.objects.filter(polling_unit_uniqueid=polling_unit_id)
    return render(request, "election/polling_units.html", {"pu_results": pu_results, "pu_form": pu_form})


def display_poll_units_total(request):
    lga_form = LocalGovtSelectionForm()
    lga_results = ''
    total_results = {}
    all_parties = Party.objects.values_list("partyname", flat=True)
    if "lga_id" in request.GET:
        lga_form = LocalGovtSelectionForm(request.GET)
        if lga_form.is_valid():
            polling_units = PollingUnit.objects.filter(lga_id=lga_form.cleaned_data["lga_id"]).values_list("uniqueid", flat=True)


            lga_results = AnnouncedPollingUnitResults.objects.filter(polling_unit_uniqueid__in=polling_units)
            for party in all_parties:
                total_results[party] = lga_results.filter(party_abbreviation=party).aggregate(total=Sum("party_score"))

    return render(request, "election/poll_total.html", {'lga_results': lga_results, 'lga_form': lga_form, "total_results": total_results})

def add_polling_unit_result(request):
    if request.method == "POST":
        polling_unit_form = PollingUnitForm(request.POST)
        agent_form = AgentForm(request.POST)
        party_form = formset_factory(PartyForm, extra=9)

        if polling_unit_form.is_valid() and agent_form.is_valid() and party_form.is_valid():
            polling_unit_form.save()
            agent_form.save()
            party_form.save()
    else:
        polling_unit_form = PollingUnitForm()
        agent_form = AgentForm()
        party_form = PartyForm()
    return render(request, "election/add_results.html", {"polling_unit_form": polling_unit_form,
                                                        "agent_form": agent_form,
                                                        "party_form": party_form})

from django.shortcuts import render
from django.http import HttpResponse
from .models import Seeds, PlantingBeds, Planted
from django.forms import ModelForm
import datetime


class SeedForm(ModelForm):
    class Meta:
        model = Seeds
        fields = ['name', 'subname', 'harvest', 'sow', 'germination', 'description', 'depth', 'light', 'spacing', 'date_on_packet']


def index(requests):
    return render(requests, 'seeds/index.html')


def seeds(requests):
    seed_data = Seeds.objects.all()
    if requests.method == "POST":
        form = SeedForm(requests.POST)
        if form.is_valid:
            form.save()
    calculate_dates(seed_data)
    return render(requests, 'seeds/seeds.html', {
        'seeds': seed_data,
        'form': SeedForm(),
    })


def beds(requests):
    return render(requests, 'seeds/beds.html', {
        "beds": PlantingBeds.objects.all()
    })


def planting(requests):
    return render(requests, 'seeds/planting.html', {
        "seeds": Seeds.objects.all(),
        "beds": PlantingBeds.objects.all()
    })


def planted(requests):
    #planted_now = Planted.objects.all()
    # need to calculate date from planted_date and germination/harvest days...somehow
    return render(requests, 'seeds/planted.html', {
        "planted": Planted.objects.all(),
    })


def name_clean_up(data):
    """
    Clean up users input
    """
    print(data)


def calculate_dates(data):
    """
    Forcast dates based on seed data
    """
    for item in data:
        item.germination = item.date_on_packet + datetime.timedelta(days=item.germination)
        item.harvest = item.date_on_packet + datetime.timedelta(days=item.harvest)

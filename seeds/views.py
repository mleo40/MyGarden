from django.shortcuts import render
from .models import Seeds, PlantingBeds, Planted
from django.forms import ModelForm
import datetime


class SeedForm(ModelForm):
    class Meta:
        model = Seeds
        fields = ['name', 'subname', 'harvest', 'sow', 'germination', 'description', 'depth', 'light', 'spacing', 'date_on_packet']


class PlantedForm(ModelForm):
    class Meta:
        model = Planted
        fields = ['seed', 'location']


def index(requests):
    return render(requests, 'seeds/index.html')


def seeds(requests):
    seed_data = Seeds.objects.all()
    if requests.method == "POST":
        form = SeedForm(requests.POST)
        if form.is_valid:
            form.save()
    return render(requests, 'seeds/seeds.html', {
        'seeds': seed_data,
        'form': SeedForm(),
    })


def beds(requests):
    return render(requests, 'seeds/beds.html', {
        "beds": PlantingBeds.objects.all()
    })


def planting(requests):
    if requests.method == "POST":
        form = PlantedForm(requests.POST)
        if form.is_valid:
            form.save()
    return render(requests, 'seeds/planting.html', {
        "seeds": Seeds.objects.all(),
        "beds": PlantingBeds.objects.all(),
    })


def planted(requests):
    planted_now = Planted.objects.all()
    calculate_dates(planted_now)
    print(planted_now)
    # need to calculate date from planted_date and germination/harvest days...somehow
    return render(requests, 'seeds/planted.html', {
        "planted":  Planted.objects.all()
    })


def name_clean_up(data):
    """
    Clean up users input
    """


def calculate_dates(data):
    """
    Forcast dates based on seed data
    """
    for item in data:
        item.germination = item.date + datetime.timedelta(days=10)
        item.harvest = item.date + datetime.timedelta(days=45)
    return data

from django.shortcuts import render
from .models import Seeds, PlantingBeds, Planted
from django.forms import ModelForm
import datetime


class SeedForm(ModelForm):
    class Meta:
        model = Seeds
        fields = ['name',
                  'subname',
                  'brand',
                  'date_on_packet',
                  'description',
                  'sow',
                  'depth',
                  'spacing',
                  'light',
                  'water',
                  'germination',
                  'harvest',
                  ]

# trying to uppercase everything:
#    def clean(self):
#        try:
#            return dict([(k, v.strip().upper()) for k, v in self.cleaned_data.items()])
#        except AttributeError:
#            pass


class PlantedForm(ModelForm):
    class Meta:
        model = Planted
        fields = ['seed', 'date', 'location']


class PlantingBedForm(ModelForm):
    class Meta:
        model = PlantingBeds
        fields = ['zone', 'bed_number']


def index(requests):
    return render(requests, 'seeds/index.html')


def seeds(requests):
    if requests.method == "POST":
        form = SeedForm(requests.POST)
        if form.is_valid:
            form.save()
    return render(requests, 'seeds/seeds.html', {
        'seeds': Seeds.objects.all().order_by('name'),
        'form': SeedForm(),
    })


def beds(requests):
    if requests.method == "POST":
        form = PlantingBedForm(requests.POST)
        if form.is_valid():
            form.save
    return render(requests, 'seeds/beds.html', {
        'beds': PlantingBeds.objects.all().order_by('zone'),
        'form': PlantingBedForm(),
    })


def planting(requests):
    return render(requests, 'seeds/planting.html', {
        "planting": Planted.objects.all(),
    })


def planted(requests):
    if requests.method == "POST":
        form = PlantedForm(requests.POST)

        ### DO MATH HERE
        # get germination and harvast days
        # add them to the date_planted
        # append planted with calculated dates
        if form.is_valid:
            form.save()
    return render(requests, 'seeds/planted.html', {
        'planted':  Planted.objects.all().order_by('seed'),
        'form': PlantedForm(),
    })


def calculate_dates(data):
    """
    Forcast dates based on seed data
    """
    for item in data:
        item.germination = item.date + datetime.timedelta(days=10)
        item.harvest = item.date + datetime.timedelta(days=45)
    return data

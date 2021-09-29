from django.shortcuts import render
from django.http import HttpResponse
from .models import Seeds, PlantingBeds, Planted


def index(requests):
    return render(requests, 'seeds/index.html')


def seeds(requests):
    seed_data = Seeds.objects.all()
    for seed in seed_data:
        print(seed)
    return render(requests, 'seeds/seeds.html', {
        "seeds": Seeds.objects.all()
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

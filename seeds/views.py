from django.shortcuts import render
from django.http import HttpResponse
from .models import Seeds


def index(requests):
    return HttpResponse("my garden")


def seeds(requests):
    return render(requests, 'seeds/seeds.html', {
        "seeds": Seeds.objects.all()
    })


def beds(requests):
    return render(requests, 'seeds/beds.html')


def planting(requests):
    return render(requests, 'seeds/planting.html')

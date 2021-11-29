from django.contrib import admin
from .models import Seeds, PlantingBeds, Planted

# Register your models here.
admin.site.register(Seeds)
admin.site.register(PlantingBeds)
admin.site.register(Planted)

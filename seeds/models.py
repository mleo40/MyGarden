from django.db import models
from django.utils import timezone


class Seeds(models.Model):
    """
    Data for seeds
    """
    light_options = (("1", "shade"),
                     ("2", "partial sun"),
                     ("3", "full sun")
                     )

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    sow = models.DateField(default="2022-05-04")
    subname = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=128)
    germination = models.IntegerField(blank=True)
    date_on_packet = models.DateField(blank=True)
    depth = models.CharField(max_length=10)
    light = models.CharField(max_length=1, choices=light_options, blank=True)
    spacing = models.CharField(max_length=10)
    harvest = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.subname}"


class PlantingBeds(models.Model):
    """
    Planting bed object
    """
    id = models.AutoField(primary_key=True)
    zone = models.CharField(max_length=64,
                            default=1,
                            choices=[('GH', 'Green house'),
                                     ('Z1', 'Zone One'),
                                     ('Z2', 'Zone Two'),
                                     ('Z3', 'Zone Three'),
                                     ('Z4', 'Zone Four'),
                                     ('Z5', 'Zone Five'),
                                     ('ID', 'Indoors')])
    bed_number = models.IntegerField()

    def __str__(self):
        return f"{self.zone} {self.bed_number}"


class Planted(models.Model):
    """
    What's actually been planted
    """
    id = models.AutoField(primary_key=True)
    seed = models.ForeignKey(Seeds, on_delete=models.CASCADE, related_name='planteds')
    location = models.ForeignKey(PlantingBeds, on_delete=models.CASCADE, related_name='planteds')
    date = models.DateField(default=timezone.now, blank=True)
    date_germination = models.DateField(default="2022-05-04", blank=True)
    date_harvest = models.DateField(default="2022-05-04", blank=True)

    def __str__(self):
        return f"{self.seed} {self.location}"

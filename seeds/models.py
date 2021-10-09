from django.db import models
from django.utils import timezone


class Seeds(models.Model):
    """
    Data for seeds
    """
    light_options = (("Full sun", "Full sun"),
                     ("Partial sun", "Partial sun"),
                     ("Shade", "Shade"),
                     ("Green house", "Green House")
                     )

    water_options = (("Minimal", "Minimal"),
                     ("Normal", "Normal"),
                     ("Heavy", "Heavy"),
                     )

    id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=64)
    sow = models.DateField(default="2022-05-04")
    subname = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=128)
    germination = models.IntegerField()
    date_on_packet = models.DateField()
    depth = models.CharField(max_length=10)
    light = models.CharField(max_length=20, choices=light_options, default="Full Sun")
    water = models.CharField(max_length=10, choices=water_options, blank=True)
    spacing = models.CharField(max_length=10)
    harvest = models.IntegerField()

    class Meta:
        constraints = [models.constraints.UniqueConstraint(fields=['name', 'subname'], name='Uniqueseed')]

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
    things_planted_here = models.ManyToManyField("Planted", related_name='plantingbedss')

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

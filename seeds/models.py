from django.db import models


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
        return f"{self.name} {self.subname} {self.harvest} {self.light}"


class PlantingBeds(models.Model):
    """
    Planting bed object
    """
    id = models.AutoField(primary_key=True)
    zone = models.IntegerField(default=1, choices=((6, "Green house"),
                                                   (1, "One"),
                                                   (2, "Two"),
                                                   (3, "Three"),
                                                   (4, "Four"),
                                                   (5, "Five")))
    bed_number = models.IntegerField()

    def __str__(self):
        return f"{self.zone} {self.bed_number}"


class Planted(models.Model):
    """
    What's actually been planted
    """
    id = models.AutoField(primary_key=True)
    seed = models.ForeignKey(Seeds, on_delete=models.CASCADE, related_name='name2')
    location = models.ForeignKey(PlantingBeds, on_delete=models.CASCADE, related_name='bed_number2')
    date = models.DateField()

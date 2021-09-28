from django.db import models


class seeds(models.Model):
    """
    Creates dbase data for seeds
    """
    light_options = [(1, "shade"),
                     (2, "partial sun"),
                     (3, "full sun")
                     ]

    name = models.CharField(max_lenght=64)
    subname = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    germination = models.IntegerField()
    date_on_packet = models.DateField()
    depth = models.IntegerField()
    light = models.Choices(select=light_options)
    spacing = models.IntegerField()
    harvest = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.subname}"

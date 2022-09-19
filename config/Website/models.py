from django.db import models


class Matchs(models.Model):
    CHOICES = (
        ("Exterieur", "Exterieur"),
        ("Domicile", "Domicile"))
    hour = models.CharField(max_length=5)
    date = models.DateField()
    location = models.CharField(max_length=100, choices=CHOICES)


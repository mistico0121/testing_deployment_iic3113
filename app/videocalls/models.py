from django.db import models

class Videocall(models.Model):
    url = models.CharField(max_length=1000)

class Survey(models.Model):
    quality = models.CharField(max_length=500)
    usefullness = models.CharField(max_length=500)
    quality_rating = models.PositiveSmallIntegerField()
    usefullness_rating = models.PositiveSmallIntegerField()
    pass

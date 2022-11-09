from django.db import models

class SeasonTicket(models.Model):
    name_season = models.CharField(max_length=255)
    price_season = models.PositiveIntegerField()
    
class Uniforms(models.Model):
    name_ski = models.CharField(max_length=255)
    size_ski = models.PositiveIntegerField()
    number_ski = models.PositiveIntegerField()
    size_boots = models.PositiveIntegerField()
    number_boots = models.PositiveIntegerField()
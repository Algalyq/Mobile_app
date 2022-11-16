from django.db import models
from django.contrib.gis.db import models as gis_models
SUBSCRIPTION_DIR = [
    ('Econom','Econom'),
    ('Business','Business'),
]


class Resort_directory(models.Model):

    resort_name = models.CharField(max_length=255, blank=False)
    resort_address = models.CharField(max_length=1024)

    def __str__(self):
        return self.resort_name
    
class Subsc_directory(models.Model):
    resort_subsc = models.ForeignKey(Resort_directory,related_name='subsc',on_delete=models.CASCADE)
    subscription = models.CharField(choices=SUBSCRIPTION_DIR,max_length=20, default='Econom')
    cost_subscr = models.PositiveIntegerField()

class Ski_directory(models.Model):
    resort_ski = models.ForeignKey(Resort_directory,related_name='ski',on_delete=models.CASCADE)
    ski_size = models.PositiveIntegerField()
    ski_count = models.PositiveIntegerField()
    ski_rent_cost = models.PositiveIntegerField()

class Boot_directory(models.Model):
    resort_boot = models.ForeignKey(Resort_directory,related_name='boot',on_delete=models.CASCADE)
    boots_size = models.PositiveIntegerField()
    boots_count = models.PositiveIntegerField()
    boots_rent_cost = models.PositiveIntegerField()


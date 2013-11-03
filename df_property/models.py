from django.db import models
from django.conf import settings


class Property(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=1, blank=True, choices=settings.RACE_CHOICES)

    req_level = models.PositiveIntegerField(default=1)

    cost_gold = models.PositiveIntegerField(default=1)
    cost_darktotem = models.PositiveIntegerField(default=0)

    attack_effect = models.IntegerField(default=1)
    shield_effect = models.IntegerField(default=1)

    req_properties = models.ManyToManyField('self', symmetrical=False, blank=True)

    #TODO: req_time for build

    def __unicode__(self):
        return "%s %s" % (self.race, self.name)
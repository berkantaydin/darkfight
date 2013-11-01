from django.db import models


class FirstName(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name


class LastName(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name
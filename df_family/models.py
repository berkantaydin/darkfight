from django.db import models
from df_account.models import User


class Family(models.Model):
    owner = models.OneToOneField(User)
    name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return "%s ( %s )" % (self.name, self.owner.username)


class FamilyMember(models.Model):
    family = models.OneToOneField(Family)
    profile = models.OneToOneField(User)
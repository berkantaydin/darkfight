from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from registration.signals import user_registered


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    race = models.CharField(max_length=1, choices=settings.RACE_CHOICES)

    exp = models.PositiveIntegerField(default=1)
    level = models.PositiveIntegerField(default=1)

    # need for missions
    energy_now = models.PositiveIntegerField(default=1)
    energy_max = models.PositiveIntegerField(default=1)

    # need for attack
    stamina_now = models.PositiveIntegerField(default=1)
    stamina_max = models.PositiveIntegerField(default=1)

    health_now = models.PositiveIntegerField(default=1)
    health_max = models.PositiveIntegerField(default=1)

    gold = models.PositiveIntegerField(default=1)

    unused_point = models.IntegerField(default=0)
    energy_point = models.IntegerField(default=1)
    stamina_point = models.IntegerField(default=1)
    health_point = models.IntegerField(default=1)
    attack_point = models.IntegerField(default=1)
    shield_point = models.IntegerField(default=1)

    def __unicode__(self):
        return unicode(self.user)

    def get_attack(self):
        if self.race == 'v':
            return (self.level + self.attack_point) * 3
        if self.race == 'w':
            return (self.level + self.attack_point) * 2

    def get_shield(self):
        if self.race == 'v':
            return (self.level + self.shield_point) * 2
        if self.race == 'w':
            return (self.level + self.shield_point) * 3

    def get_energy(self):
        return self.energy_now

    def get_stamina(self):
        return self.stamina_now


def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    profile.race = request.POST["race"]
    profile.save()


user_registered.connect(user_registered_callback)

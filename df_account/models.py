from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from registration.signals import user_registered
from df_char.models import FirstName, LastName
from df_family.models import Family
from df_property.models import Property


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    race = models.CharField(max_length=1, choices=settings.RACE_CHOICES)
    first_name = models.ForeignKey(FirstName, null=True)
    last_name = models.ForeignKey(LastName, null=True)

    # TODO : Need null True for admin panel while edit
    family = models.ForeignKey(Family, null=True)

    exp = models.PositiveIntegerField(default=1)
    level = models.PositiveIntegerField(default=1)

    # need for missions
    energy_now = models.PositiveIntegerField(default=1)

    # need for attack
    stamina_now = models.PositiveIntegerField(default=1)

    health_now = models.PositiveIntegerField(default=1)

    gold = models.PositiveIntegerField(default=1)
    darktotem = models.PositiveIntegerField(default=1)

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
        return (self.energy_point * 4) + self.level

    def get_stamina(self):
        return (self.stamina_point * 2) + self.level

    def get_health(self):
        return (self.health_point * 5) + (self.level * 12)

    def exp_need_for_next_level(self):
        return self.level + (self.level * self.level) + 9


def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    profile.race = request.POST["race"]
    profile.first_name = FirstName.objects.order_by('?')[0]
    profile.last_name = LastName.objects.order_by('?')[0]
    profile.save()


user_registered.connect(user_registered_callback)


class UserProperties(models.Model):
    user = models.OneToOneField(User)
    property = models.ForeignKey(Property)
    piece = models.PositiveIntegerField(default=1)
from django import forms
from django.conf import settings

from registration.forms import RegistrationForm


class ExRegistrationForm(RegistrationForm):
    race = forms.ChoiceField(label = "Irk",choices=settings.RACE_CHOICES)
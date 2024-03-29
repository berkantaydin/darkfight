from django.conf.urls import patterns, include, url

from registration.backends.default.views import RegistrationView

from .forms import UserRegistrationForm


"""
    http://johnparsons.net/index.php/2013/06/28/creating-profiles-with-django-registration/
"""

urlpatterns = patterns('',
                       url(r'^register/$',
                           RegistrationView.as_view(form_class=UserRegistrationForm),
                           name='registration_register'),

                       (r'', include('registration.backends.default.urls')),
)
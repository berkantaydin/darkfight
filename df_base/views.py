from django.shortcuts import render
from df_account.forms import ExRegistrationForm


def landing(request):
    if not request.user.is_authenticated():
        return render(request, 'base_not_logged_in.html', dict(form_registration=ExRegistrationForm()))
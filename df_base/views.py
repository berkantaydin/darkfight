from django.shortcuts import render, HttpResponse
from df_account.forms import UserRegistrationForm


def landing(request):
    if request.user.is_authenticated():
        return HttpResponse("loggedin")
    else:
        return render(request, 'base_not_logged_in.html', dict(form_registration=UserRegistrationForm()))
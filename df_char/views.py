from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from df_account.models import UserProfile


@login_required
def profile(request, username):
    # TODO: If User exists but profile not exists status?
    profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'df_char/profile.html', dict(profile=profile, race=settings.RACE_CHOICES))
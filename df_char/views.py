# -*- coding: utf-8 -*-
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from df_account.models import UserProfile


@login_required
def profile(request, username):
    # TODO: If User exists but profile not exists status?
    profile = get_object_or_404(UserProfile, user__username=username)
    if profile.unused_point > 0:
        messages.info(request, 'Dağıtılmamış Yetenek Puanlarınız Var.')
    return render(request, 'df_char/profile.html', dict(profile=profile, race=settings.RACE_CHOICES))


@login_required
def use_point(request, field):
    profile = get_object_or_404(UserProfile, user__username=request.user)
    if profile.unused_point > 0:
        if field == 'energy':
            profile.energy_point += 1
        if field == 'stamina':
            profile.stamina_point += 1
        if field == 'health':
            profile.health_point += 1
        if field == 'attack':
            profile.attack_point += 1
        if field == 'shield':
            profile.shield_point += 1
        if field in ('energy', 'stamina', 'health','attach','shield'):
            profile.unused_point -= 1
            profile.save()
            messages.success(request, 'Puan Başarıyla Kullanıldı.')
    else:
        messages.error(request, 'Tüm yetenek puanlarınız kullanılmış.')
    return redirect('char_profile', username=profile.user.username)
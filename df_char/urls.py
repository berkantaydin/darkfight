from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'profile/(?P<username>[\w-]*)$', 'df_char.views.profile', name='char_profile'),
)
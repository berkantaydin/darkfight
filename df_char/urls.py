from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'profile/(?P<username>[\w-]*)$', 'df_char.views.profile', name='char_profile'),
                       url(r'profile/use_point/(?P<field>[\w-]*)$', 'df_char.views.use_point', name='char_use_point'),
)
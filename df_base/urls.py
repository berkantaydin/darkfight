from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^$', 'df_base.views.landing', name='base_landing'),
)
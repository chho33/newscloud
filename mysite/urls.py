from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'', 'newsCloud.views.home', name='home'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'', include('newsCloud.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()

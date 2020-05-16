from django.conf.urls import include, url
from django.contrib import admin

#admin.autodiscover()

urlpatterns = [
    url(r'^histograms$', include('technique_challenge_addons.histograms.urls')),
]

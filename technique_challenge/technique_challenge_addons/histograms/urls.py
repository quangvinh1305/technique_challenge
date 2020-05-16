from django.conf.urls import url
from django.contrib import admin
from technique_challenge_addons.histograms.views import HistogramsView
#admin.autodiscover()

app_name = 'histograms'
urlpatterns = [
    url(r'^$'.format(app_name),
        HistogramsView.as_view(), name='histograms-words'),
]
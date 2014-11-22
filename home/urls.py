from django.conf.urls import patterns, url

from home.views import *

urlpatterns = patterns('',
    url(r'^$', HomeIndexView.as_view(), name='homeIndex'),
    url(r'^errorMsg/\d{3}$', HomeIndexView.as_view(), name='homeIndex'),
)
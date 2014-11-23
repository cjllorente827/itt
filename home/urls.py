from django.conf.urls import patterns, url

from home.views import *

"""
Url pattern matching convention distinguishes between page view requests and REST calls
Pageview request patterns MUST use GET and may not contain the word 'api'. They should dispatch to a method that
begins with 'view_'.

REST calls MUST be prefixed with 'api' and can use one of GET, POST, PUT, or DELETE which must be mapped to a method
that begins with 'read_', 'create_', 'update_', or 'delete_', respectively.
"""

urlpatterns = patterns('',
    url(r'^$', HomeIndexView.as_view(), name='homeIndex'),
    url(r'^errorMsg/\d{3}$', HomeIndexView.as_view(), name='homeIndex'),
)
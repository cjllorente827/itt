from django.conf.urls import patterns, url

from home.util import method_dispatch
from channel import views, api

"""
Url pattern matching convention distinguishes between page view requests and REST calls
Pageview request patterns MUST use GET and may not contain the word 'api'. They should dispatch to a method that
begins with 'view_'.

REST calls MUST be prefixed with 'api' and can use one of GET, POST, PUT, or DELETE which must be mapped to a method
that begins with 'read_', 'create_', 'update_', or 'delete_', respectively.
"""

urlpatterns = patterns('c',
	url(
		r'^$', 
		views.index),
	url(
		r'^api/channel/(?P<channel_id>\d+)$',
		method_dispatch(GET = api.read_channel)),
	url(
		r'^api/channel/(?P<channel_id>\d+)/messages$',  
		method_dispatch(GET = api.read_channel_messages)),
	url(
		r'^api/channel/(?P<channel_id>\d+)/messages/(?P<timestamp>\d+)$',  
		method_dispatch(GET = api.read_new_channel_messages)),
	url(
		r'^api/message$',  
		method_dispatch(POST = api.create_message)),
)
from django.conf.urls import patterns, url

from home.util import method_dispatch
from thread import views

"""
Url pattern matching convention distinguishes between page view requests and REST calls
Pageview request patterns MUST use GET and may not contain the word 'api'. They should dispatch to a method that
begins with 'view_'.

REST calls MUST be prefixed with 'api' and can use one of GET, POST, PUT, or DELETE which must be mapped to a method
that begins with 'read_', 'create_', 'update_', or 'delete_', respectively.
"""

urlpatterns = patterns('',
	url(
		r'^$', 
		views.index),
	url(
		r'^(?P<thread_id>\d+)$',  
		method_dispatch(GET = views.view_thread)),
	url(
		r'^api/thread/(?P<thread_id>\d+)$',
		method_dispatch(GET = views.read_thread)),
	url(
		r'^api/thread/(?P<thread_id>\d+)/messages$',  
		method_dispatch(GET = views.read_thread_messages)),
	url(
		r'^api/message$',  
		method_dispatch(POST = views.create_message)),
)
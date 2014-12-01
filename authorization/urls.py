from django.conf.urls import patterns, url

from authorization import views, api
from home.util import method_dispatch

"""
Url pattern matching convention distinguishes between page view requests and REST calls
Pageview request patterns MUST use GET and may not contain the word 'api'. They should dispatch to a method that
begins with 'view_'.

REST calls MUST be prefixed with 'api' and can use one of GET, POST, PUT, or DELETE which must be mapped to a method
that begins with 'read_', 'create_', 'update_', or 'delete_', respectively.
"""

urlpatterns = patterns('auth',
	url(
		r'^api/login$', 
		method_dispatch(POST=api.user_login)),
	url(
		r'^api/logout$', 
		method_dispatch(GET=api.user_logout)),
	url(
		r'^api/register$', 
		method_dispatch(POST=api.create_user)),
)
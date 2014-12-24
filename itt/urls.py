from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(
		r'^', 
		include('home.urls', namespace="home")),
	url(
		r'^auth/', 
		include('authorization.urls', namespace="authorization")),
	url(
		r'^t/', 
		include('thread.urls', namespace="thread")),
	url(
		r'^u/', 
		include('user.urls', namespace="user")),
	url(
		r'^admin/', 
		include(admin.site.urls)),
)


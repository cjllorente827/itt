from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^', include('home.urls', namespace="home")),
	url(r'^threads/', include('threads.urls', namespace="threads")),
	url(r'^stylesheets/', include('stylesheets.urls', namespace="stylesheets")),
    url(r'^account/', include('account.urls', namespace="account")),
    url(r'^admin/', include(admin.site.urls)),
)